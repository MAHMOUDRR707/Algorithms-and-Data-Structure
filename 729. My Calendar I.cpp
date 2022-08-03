class MyCalendar {
    
public:
    vector<pair<int,int>>  res;
    MyCalendar() {
         
    }
    
    bool book(int start, int end) {
        for(auto i : res){
            int x = i.first;
            int y = i.second;
            if (x <  end  && start < y ) return false;
        }
        res.push_back({start,end});
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
