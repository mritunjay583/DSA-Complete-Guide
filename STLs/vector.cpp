#include<iostream>

#include<bits/stdc++.h>

// push_back(): Adds an element to the end of the vector. O(1) amortized time.
// pop_back(): Removes the last element from the vector. O(1) time.
// size(): Returns the number of elements in the vector. O(1) time.
// empty(): Checks if the vector is empty. O(1) time.
// clear(): Removes all elements from the vector. O(n) time.
// resize(): Changes the size of the vector. O(n) time.
// front(): Returns a reference to the first element. O(1) time.
// back(): Returns a reference to the last element. O(1) time.


using namespace std;

void multipleWaysToInitializeVectors(){
    vector<int> vec1; // Empty vector
    vector<int> vec2(5, 2); // Vector with size 5 initialized to 2
    vector<int> vec3 = {1, 2, 3, 4, 5}; // Vector initialized with values
    vector<int> vec4(5); // vector with size 5 initialized with 0
}

void print2DVector(vector<vector<int>>& vec){
    for (const auto& row : vec) {
        for (int num : row) {
            cout << num << " ";
        }
        cout << endl;
    }
    cout<<"\n\n"<<endl;
}

void initialize2DVectorNested() {
    vector<vector<int>> vec1 = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    int rows = 3, cols = 3;

    vector<vector<int>> vec2;
    vec2.resize(rows, vector<int>(cols, 0));

    vector<vector<int>> vec3(rows, vector<int>(cols));

    print2DVector(vec1);
    print2DVector(vec2);
    print2DVector(vec3);

}

void printVector(const vector<int>& vec){
    for(auto element:vec){
        cout<<element<<" ";
    }
    cout<<endl;
}

void vectorOperations(){
    cout<<"vector operations-------------"<<endl;
    vector<int> vec = {1, 2, 3, 4, 5};
    printVector(vec);
    vec.push_back(10);
    vec.push_back(12);
    printVector(vec);

    vec.pop_back();
    printVector(vec);
    
    cout<<"size of vector: "<<vec.size()<<endl;
    cout<<"vector.empty(): "<<vec.empty()<<endl;
    cout<<"vector.front(): "<<vec.front()<<endl;
    cout<<"vector.back(): "<<vec.back()<<endl;

    vec.clear();
    cout<<"vector.clear(): ";
    printVector(vec);
}

void resizeVector(){
    cout<<"vector resize------------------ "<<endl;
    vector<int> vec = {1, 2, 3, 4, 5};
    printVector(vec);

    // Resize the vector to contain 8 elements (additional elements will be default-initialized to 0)
    vec.resize(8);
    // Output: 1 2 3 4 5 0 0 0
    printVector(vec);

    // Resize the vector to contain 3 elements (excess elements will be removed)
    vec.resize(3);
    // Output: 1 2 3
    printVector(vec);

    // Resize the vector to contain 5 elements with the value 10
    vec.resize(5, 10);
    // Output: 1 2 3 10 10
    printVector(vec);
}

int main(){
    initialize2DVectorNested();
    // vectorOperations();
    // resizeVector();
    return 0;
}