#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>

struct ReverseCheck {
    std::array<std::array<int,4>,144> neighbors{};
    std::array<int,144> weights{};
    const std::array<int,4> towers{22,1,13,25};
    ReverseCheck() {
        const int dx[4]{1,0,-1,0}, dy[4]{0,1,0,-1};
        for(int v=0;v<144;++v) {
            for(int t:towers) {
                int ax=std::abs(v%12-t%12), ay=std::abs(v/12-t/12);
                if(std::max(ax,ay)==1) ++weights[v];
            }
            for(int d=0;d<4;++d) {
                int x=v%12+dx[d], y=v/12+dy[d];
                neighbors[v][d]=(x>=0&&x<12&&y>=0&&y<12)?x+12*y:-1;
            }
        }
    }
    int score(const std::array<uint8_t,5>& row, int& cardinality) const {
        std::array<bool,144> blocked{};
        for(int t:towers) blocked[t]=true;
        cardinality=0;
        bool padded=false;
        int previous=-1;
        for(int i=0;i<4;++i) {
            int v=row[i];
            if(v==255){padded=true;continue;}
            if(padded||v<=previous||v<=0||v>=143||blocked[v])
                throw std::runtime_error("Invalid record wall cells");
            blocked[v]=true;previous=v;++cardinality;
        }
        if(row[4]>33) throw std::runtime_error("Invalid recorded score");
        std::array<int,144> distance;
        distance.fill(-1);
        std::array<int,144> queue{};
        int head=0, tail=1;
        queue[0]=143;distance[143]=0;
        while(head<tail) {
            int vertex=queue[head++];
            // Reverse neighbor order is deliberately immaterial to distances.
            for(int d=3;d>=0;--d) {
                int next=neighbors[vertex][d];
                if(next<0||blocked[next]||distance[next]>=0)continue;
                distance[next]=distance[vertex]+1;
                queue[tail++]=next;
            }
        }
        if(distance[0]<0)return -1;
        int vertex=0, value=0, steps=0;
        while(vertex!=143) {
            value+=weights[vertex];
            int chosen=-1;
            for(int next:neighbors[vertex]) {
                if(next>=0&&!blocked[next]&&distance[next]==distance[vertex]-1) {
                    chosen=next;break;
                }
            }
            if(chosen<0||++steps>143)throw std::runtime_error("Invalid descending path");
            vertex=chosen;
        }
        return value;
    }
};

int main(int argc,char** argv) {
    try {
        if(argc!=3)throw std::runtime_error("Expected input and output arguments");
        std::ifstream input(argv[1],std::ios::binary);
        if(!input)throw std::runtime_error("Cannot read input");
        ReverseCheck check;
        std::array<uint64_t,5> counts{}, invalid{};
        std::array<std::array<uint64_t,34>,5> histogram{};
        std::array<int,5> maxima{-1,-1,-1,-1,-1};
        uint64_t total=0, mismatch=0;
        auto begin=std::chrono::steady_clock::now();
        std::array<uint8_t,5> row{};
        while(input.read(reinterpret_cast<char*>(row.data()),5)||input.gcount()) {
            if(input.gcount()!=5)throw std::runtime_error("Truncated record");
            int k=0, value=check.score(row,k);
            if(value< -1||value>32)throw std::runtime_error("Unexpected exposure range");
            ++counts[k];++histogram[k][value+1];++total;
            if(value<0)++invalid[k];
            maxima[k]=std::max(maxima[k],value);
            if(value!=static_cast<int>(row[4])-1) {
                if(mismatch<64) {
                    std::cerr<<"{\"record\":"<<total-1<<",\"expected\":"<<static_cast<int>(row[4])-1
                             <<",\"actual\":"<<value<<",\"walls\":[";
                    for(int i=0;i<k;++i){if(i)std::cerr<<',';std::cerr<<static_cast<int>(row[i]);}
                    std::cerr<<"]}\n";
                }
                ++mismatch;
            }
        }
        if(!input.eof())throw std::runtime_error("Input read failure");
        double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-begin).count();
        std::ofstream output(argv[2]);
        if(!output)throw std::runtime_error("Cannot write output");
        output<<"{\"records\":"<<total<<",\"mismatches\":"<<mismatch<<",\"elapsed_seconds\":"<<seconds<<",\"cardinalities\":[";
        for(int k=0;k<5;++k) {
            if(k)output<<',';
            output<<"{\"k\":"<<k<<",\"count\":"<<counts[k]<<",\"invalid\":"<<invalid[k]<<",\"maximum\":"<<maxima[k]<<",\"histogram\":[";
            for(int i=0;i<34;++i){if(i)output<<',';output<<histogram[k][i];}
            output<<"]}";
        }
        output<<"]}\n";
        if(!output)throw std::runtime_error("Output write failure");
        return mismatch?2:0;
    } catch(const std::exception& error) {
        std::cerr<<error.what()<<'\n';return 1;
    }
}
