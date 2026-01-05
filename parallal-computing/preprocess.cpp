#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <omp.h>

using namespace std;

#define IMAGE_SIZE 784
#define NUM_CLASSES 10

// Dataset structure (MUST be before usage)
struct Dataset {
    vector<vector<float>> X;
    vector<vector<int>> y;
};

// One-hot encoding
vector<int> oneHotEncode(int label) {
    vector<int> encoded(NUM_CLASSES, 0);
    encoded[label] = 1;
    return encoded;
}

// Safe MNIST loader
Dataset loadMNIST(const string& filename) {
    Dataset data;
    ifstream file(filename);
    string line;

    // Skip header row
    getline(file, line);

    while (getline(file, line)) {

        if (line.empty()) continue;

        stringstream ss(line);
        string value;

        // Read label safely
        if (!getline(ss, value, ',')) continue;
        if (value.find_first_not_of("0123456789") != string::npos) continue;

        int label = stoi(value);
        data.y.push_back(oneHotEncode(label));

        vector<float> image(IMAGE_SIZE);

        for (int i = 0; i < IMAGE_SIZE; i++) {
            if (!getline(ss, value, ',')) value = "0";
            image[i] = stof(value) / 255.0f;  // Normalization
        }

        data.X.push_back(image);
    }

    return data;
}

// Parallel dataset split
void splitDataset(const Dataset& full,
                  Dataset& train,
                  Dataset& val,
                  Dataset& test) {

    int total = full.X.size();
    int trainEnd = total * 0.7;
    int valEnd = total * 0.85;

    #pragma omp parallel for
    for (int i = 0; i < total; i++) {
        if (i < trainEnd) {
            #pragma omp critical
            {
                train.X.push_back(full.X[i]);
                train.y.push_back(full.y[i]);
            }
        } else if (i < valEnd) {
            #pragma omp critical
            {
                val.X.push_back(full.X[i]);
                val.y.push_back(full.y[i]);
            }
        } else {
            #pragma omp critical
            {
                test.X.push_back(full.X[i]);
                test.y.push_back(full.y[i]);
            }
        }
    }
}

int main() {
    omp_set_num_threads(4);

    cout << "Loading MNIST dataset..." << endl;
    Dataset fullData = loadMNIST("mnist_train.csv");

    Dataset train, val, test;
    splitDataset(fullData, train, val, test);

    cout << "\nDataset Split Completed" << endl;
    cout << "Training samples   : " << train.X.size() << endl;
    cout << "Validation samples : " << val.X.size() << endl;
    cout << "Test samples       : " << test.X.size() << endl;

    return 0;
}


