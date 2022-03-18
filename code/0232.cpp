class MyQueue {
public:
    stack<int> stk1;
    stack<int> stk2;
    MyQueue() {
    }
    
    void push(int x) {
        stk1.push(x);
    }
    
    int pop() {
        pour();
        int out = stk2.top();
        stk2.pop();
        return out;
    }
    
    int peek() {
        pour();
        return stk2.top();
    }
    
    bool empty() {
        pour();
        return stk2.size() == 0;
    }
    void pour(){
        if(stk2.size() == 0){
            while(stk1.size() != 0){
                stk2.push(stk1.top());
                stk1.pop();
            }
        }
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */