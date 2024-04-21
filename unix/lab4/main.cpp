#include <iostream>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <linux/input.h>

using namespace std;

// for start program enter next commands: 
// g++ main.cpp -o main
// sudo ./main

int main () 
{
    cout << "WORK" << endl;
    const char *device = "/dev/input/event2"; 
    int fd = open(device, O_RDONLY);
    if (fd == -1) {
        perror("Failed to open device");
        return 1;
    }

    struct input_event ev;
    while (1) {
        ssize_t n = read(fd, &ev, sizeof(ev));
        if (n == sizeof(ev)) {
            if (ev.type == EV_KEY && ev.value == 1) {
                printf("Key code: %d\n", ev.code);
            }
        }
    }

    close(fd);
    return 0;
}