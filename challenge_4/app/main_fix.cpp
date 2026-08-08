#include <iostream>
#include <string>

int main() {
    std::string buf;
    std::cout << "Jmeno> ";
    std::getline(std::cin, buf);
    if (buf.size() > 16) buf.resize(16);
    std::cout << "Ahoj " << buf << "\n";
    return 0;
}
