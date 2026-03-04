#include <iostream>
#include <pthread.h>
#include <vector>
#include <chrono>
#include <cstdlib>

using namespace std;
using namespace std::chrono;

#define NUM_THREADS 4

vector<int> arr;
long long global_sum = 0;
bool found = false;
int key;

// Structure for thread data
struct ThreadData {
    int start;
    int end;
};

// ================= SEQUENTIAL =================
long long sequential_sum() {
    long long sum = 0;
    for(int i = 0; i < arr.size(); i++)
        sum += arr[i];
    return sum;
}

bool sequential_search() {
    for(int i = 0; i < arr.size(); i++)
        if(arr[i] == key)
            return true;
    return false;
}

// ================= THREAD FUNCTIONS =================
void* threaded_sum(void* arg) {
    ThreadData* data = (ThreadData*)arg;
    long long local_sum = 0;

    for(int i = data->start; i < data->end; i++)
        local_sum += arr[i];

    __sync_fetch_and_add(&global_sum, local_sum);
    pthread_exit(NULL);
}

void* threaded_search(void* arg) {
    ThreadData* data = (ThreadData*)arg;

    for(int i = data->start; i < data->end; i++) {
        if(arr[i] == key) {
            found = true;
            break;
        }
    }
    pthread_exit(NULL);
}

// ================= MAIN =================
int main() {

    int n;
    cout << "Enter array size: ";
    cin >> n;

    arr.resize(n);

    // Generate random array
    for(int i = 0; i < n; i++)
        arr[i] = rand() % 1000;

    cout << "Enter key to search: ";
    cin >> key;

    // ---------------- SEQUENTIAL ----------------
    auto start = high_resolution_clock::now();
    long long seq_sum = sequential_sum();
    auto stop = high_resolution_clock::now();
    auto duration_sum_seq = duration_cast<microseconds>(stop - start);

    start = high_resolution_clock::now();
    bool seq_found = sequential_search();
    stop = high_resolution_clock::now();
    auto duration_search_seq = duration_cast<microseconds>(stop - start);

    // ---------------- THREADED ----------------
    pthread_t threads[NUM_THREADS];
    ThreadData threadData[NUM_THREADS];

    int chunk = n / NUM_THREADS;
    global_sum = 0;
    found = false;

    start = high_resolution_clock::now();
    for(int i = 0; i < NUM_THREADS; i++) {
        threadData[i].start = i * chunk;
        threadData[i].end = (i == NUM_THREADS - 1) ? n : (i+1) * chunk;
        pthread_create(&threads[i], NULL, threaded_sum, &threadData[i]);
    }

    for(int i = 0; i < NUM_THREADS; i++)
        pthread_join(threads[i], NULL);

    stop = high_resolution_clock::now();
    auto duration_sum_thread = duration_cast<microseconds>(stop - start);

    start = high_resolution_clock::now();
    for(int i = 0; i < NUM_THREADS; i++)
        pthread_create(&threads[i], NULL, threaded_search, &threadData[i]);

    for(int i = 0; i < NUM_THREADS; i++)
        pthread_join(threads[i], NULL);

    stop = high_resolution_clock::now();
    auto duration_search_thread = duration_cast<microseconds>(stop - start);

    // ---------------- RESULTS ----------------
    cout << "\n===== RESULTS =====\n";
    cout << "Sequential Sum: " << seq_sum << endl;
    cout << "Threaded Sum: " << global_sum << endl;

    cout << "Sequential Search: " << (seq_found ? "Found" : "Not Found") << endl;
    cout << "Threaded Search: " << (found ? "Found" : "Not Found") << endl;

    cout << "\n===== EXECUTION TIME (microseconds) =====\n";
    cout << "Sequential Sum Time: " << duration_sum_seq.count() << endl;
    cout << "Threaded Sum Time: " << duration_sum_thread.count() << endl;

    cout << "Sequential Search Time: " << duration_search_seq.count() << endl;
    cout << "Threaded Search Time: " << duration_search_thread.count() << endl;

    cout << "\n===== SPEEDUP =====\n";
    cout << "Sum Speedup: "
         << (double)duration_sum_seq.count() / duration_sum_thread.count() << endl;

    cout << "Search Speedup: "
         << (double)duration_search_seq.count() / duration_search_thread.count() << endl;

    return 0;
}