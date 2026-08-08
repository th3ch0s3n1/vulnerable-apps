FROM gcc:12
WORKDIR /app
COPY app/ /app
# vypnuté ochrany
RUN g++ -std=c++17 -fno-stack-protector -no-pie -z execstack main.cpp -o main
CMD ["./main"]