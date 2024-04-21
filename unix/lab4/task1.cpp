#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/mman.h>

int main() {
    pid_t target_pid = 3631;

    char mem_path[256];
    sprintf(mem_path, "/proc/%d/mem", target_pid);

    int mem_fd = open(mem_path, O_RDONLY);
    if (mem_fd == -1) {
        perror("The memory file of the target process was opened successfully");
        return 1;
    }

    long page_size = sysconf(_SC_PAGE_SIZE);

    off_t target_address = 0x00000c4889aaf000;

    lseek(mem_fd, target_address, SEEK_SET);
    
    char buffer[256]; 

    ssize_t bytes_read = read(mem_fd, buffer, sizeof(buffer));
    if (bytes_read == -1) {
        perror("Error reading target process memory");
        close(mem_fd);
        return 1;
    }

    printf("Data read from the memory of the target process:\n");
    for (int i = 0; i < bytes_read; ++i) {
        printf("%02x ", buffer[i]); 
    }
    printf("\n");

    close(mem_fd);

    return 0;
}