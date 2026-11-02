#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

struct Enumeration {
    std::array<bool,144> blocked{};
    std::array<int,144> weight{};
    std::array<std::array<int,4>,144> neighbors{};
    std::vector<int> cells;
    std::array<uint8_t,4> selected{255,255,255,255};
    std::array<uint64_t,5> counts{}, invalid{};
    std::array<int,5> maximum{-1,-1,-1,-1,-1};
    std::array<std::array<uint8_t,4>,5> witnesses{};
    std::ofstream output;
    int shard;
    explicit Enumeration(int part,const std::string& name):output(name,std::ios::binary),shard(part) {
        if(!output || shard<0 || shard>2) throw std::runtime_error("Invalid output or shard");
        const std::array<int,4> towers{22,1,13,25};
        for(int t:towers) blocked[t]=true;
        const int dx[4]{1,0,-1,0},dy[4]{0,1,0,-1};
        for(int v=0;v<144;++v) {
            if(v!=0 && v!=143 && !blocked[v])cells.push_back(v);
            for(int t:towers) if(std::max(std::abs(v%12-t%12),std::abs(v/12-t/12))==1)++weight[v];
            for(int d=0;d<4;++d) {
                int x=v%12+dx[d], y=v/12+dy[d];
                neighbors[v][d]=(x>=0&&x<12&&y>=0&&y<12)?12*y+x:-1;
            }
        }
        if(cells.size()!=138)throw std::runtime_error("Wrong available-cell count");
    }
    int score()const {
        std::array<int,144> parents;parents.fill(-2);
        std::array<int,144> queue;int begin=0,end=1;
        queue[0]=0;parents[0]=-1;
        while(begin<end) {
            int v=queue[begin++];
            if(v==143) {
                int value=0;
                for(int p=parents[143];p!=-1;p=parents[p])value+=weight[p];
                return value;
            }
            for(int next:neighbors[v])if(next>=0 && !blocked[next] && parents[next]==-2) {
                parents[next]=v;queue[end++]=next;
            }
        }
        return -1;
    }
    void record(int k) {
        int value=score();++counts[k];
        if(value<0)++invalid[k];
        if(value>maximum[k]){maximum[k]=value;witnesses[k]=selected;}
        std::array<uint8_t,5> row{selected[0],selected[1],selected[2],selected[3],static_cast<uint8_t>(value+1)};
        output.write(reinterpret_cast<const char*>(row.data()),5);
        if(!output)throw std::runtime_error("Output write failed");
    }
    void extend(int k,int depth,int next) {
        if(depth==k){record(k);return;}
        for(int i=next;i<=static_cast<int>(cells.size())-(k-depth);++i) {
            selected[depth]=static_cast<uint8_t>(cells[i]);blocked[cells[i]]=true;
            extend(k,depth+1,i+1);
            blocked[cells[i]]=false;selected[depth]=255;
        }
    }
    void run(const std::string& meta) {
        auto start=std::chrono::steady_clock::now();
        if(shard==0)record(0);
        for(int k=1;k<=4;++k) {
            for(int i=shard;i<=static_cast<int>(cells.size())-k;i+=3) {
                selected[0]=static_cast<uint8_t>(cells[i]);blocked[cells[i]]=true;
                extend(k,1,i+1);
                blocked[cells[i]]=false;selected[0]=255;
            }
            std::cerr<<"{\"cardinality\":"<<k<<",\"records\":"<<counts[k]<<"}\n";
        }
        output.close();
        if(!output)throw std::runtime_error("Output close failed");
        double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream file(meta);
        if(!file)throw std::runtime_error("Metadata write failed");
        file<<"{\"shard\":"<<shard<<",\"elapsed_seconds\":"<<elapsed<<",\"cardinalities\":[";
        for(int k=0;k<=4;++k){
            if(k)file<<',';
            file<<"{\"k\":"<<k<<",\"count\":"<<counts[k]<<",\"invalid\":"<<invalid[k]<<",\"maximum_score\":"<<maximum[k]<<",\"witness\":[";
            for(int j=0;j<k;++j){if(j)file<<',';file<<static_cast<int>(witnesses[k][j]);}
            file<<"]}";
        }
        file<<"]}\n";
        if(!file)throw std::runtime_error("Metadata close failed");
    }
};
int main(int argc,char** argv){
    try{
        if(argc!=4)throw std::runtime_error("Expected shard, records and metadata arguments");
        Enumeration enumeration(std::stoi(argv[1]),argv[2]);enumeration.run(argv[3]);return 0;
    }catch(const std::exception& error){std::cerr<<error.what()<<'\n';return 1;}
}
