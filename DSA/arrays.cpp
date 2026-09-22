#include<iostream>
#include<string>

using namespace std;
#define INT_MAX 999999999;

struct res{
    bool present;
    int index;
};

res linearsearch(int target, int* numbers, int size){

        for(int i=0; i<size;i++){
            if(numbers[i]==target){
                return {true,i};
            }
        }
        return {false, -1};
}

//sorted array given
res binarysearch(int target, int* numbers, int size, int left, int right){
    while(left<=right){
        int m = left+(right-left)/2;
        if(numbers[m]>target) right=m-1;
        else if(numbers[m]<target) left=m+1;
        else if(numbers[m]==target) return {true, m};
    }
    return {false,-1};
}

int basics0(){

    int numbers[5];
    cout<<"Enter 5 numbers :"<<endl;

    for(int i=0; i<5;i++){
        cin>>numbers[i];
    }

     for(int i=0; i<5;i++){
        numbers[i]*=2;
    }

    for(int i=0; i<5;i++){
        cout<<numbers[i]<<endl;
    }

    return 0;

}


int basics1(){
    int numbers[5];
    cout<<"Enter 5 numbers :"<<endl;

    for(int i=0; i<5;i++){
        cin>>numbers[i];
    }
    int target;
    cout<<"Enter target"<<endl;
    cin>>target;

    res result = linearsearch(target, numbers, 5);
    res result2 = binarysearch(target, numbers, 5, 0, 4);

    if(result.present){
        cout<<"At Index: "<< result.index <<endl;
    }
    else if(!result.present){
        cout<<"not found"<<endl;
    }

    if(result2.present){
        cout<<"Binary search , At Index: "<< result2.index <<endl;
    }
    else if(!result2.present){
        cout<<"Binary Search, not found"<<endl;
    }

    return 0;

}

int findMax(){
    int numbers[5];
    cout<<"Enter 5 numbers :"<<endl;

    int max=-INT_MAX;

    for(int i=0; i<5;i++){
        cin>>numbers[i];
        if(max<numbers[i]) max=numbers[i];
    }
    cout<<max<<endl;

    return 0;

}

int findMin(){

    int numbers[5];
    cout<<"Enter 5 numbers :"<<endl;

    int min=INT_MAX;

    for(int i=0; i<5;i++){
        cin>>numbers[i];
        if(min>numbers[i]) min=numbers[i];
    }
    cout<<min<<endl;

    return 0;

}



int main(){
    //basics0();
    //basics1();
    //findMax();
    findMin();

    return 0;
    
}