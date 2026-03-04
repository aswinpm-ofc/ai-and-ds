#include <iostream>
#include <pthread.h>

using namespace std;

// Structure to pass argument to thread
struct ThreadData {
    int n;
};

// Thread function
void* printNumbers(void* arg) {
    ThreadData* data = (ThreadData*)arg;
    int n = data->n;

    cout << "Thread started. Printing first " << n << " natural numbers:\n";

    for(int i = 1; i <= n; i++) {
        cout << i << " ";
    }

    cout << "\nThread finished.\n";

    pthread_exit(NULL);
}

int main() {

    pthread_t thread;
    ThreadData data;

    cout << "Enter value of n: ";
    cin >> data.n;

    // Create thread
    if(pthread_create(&thread, NULL, printNumbers, (void*)&data)) {
        cout << "Error creating thread\n";
        return 1;
    }

    // Wait for thread to finish
    pthread_join(thread, NULL);

    cout << "Main function completed.\n";

    return 0;
}
