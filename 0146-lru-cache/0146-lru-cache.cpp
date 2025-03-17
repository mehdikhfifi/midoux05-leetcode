#include <iostream>
#include <map>

using namespace std;

class Node { 
  public: 

  int key;
  int value;
  Node *prev;
  Node *next;

    Node(int key, int value){
      this->key = key;
      this->value = value;
      this->prev = nullptr;
      this->next = nullptr; 
    }

    
};

class LRUCache {
  public:
    unordered_map<int, Node *> lrucache;
    int capacity;
    Node* head;
    Node* tail;
    
      LRUCache(int capacity) {
       
        this->capacity = capacity;
        head = new Node(0,0);
        tail = new Node(0,0);
        head->next = tail;
        tail->prev = head;
      }
      
      int get(int key) {
        // check if key is inside map

        if (lrucache.find(key) != lrucache.end()){
          remove(lrucache[key]);
          insert(lrucache[key]);
          return lrucache[key]->value;

        }
        else{
          return -1;
        }


      }
      
      void put(int key, int value) {
          
        if (lrucache.find(key) != lrucache.end()){
          
          Node* resnode = lrucache[key];
          resnode->value = value;
          remove(resnode);
          insert(resnode);
        }
        else{
          if (lrucache.size() == this->capacity){
            Node *last_item = tail->prev;
            lrucache.erase(last_item->key);
            remove(tail->prev);
          }
          Node* x = new Node(key,value);
          lrucache[key] = x;
          insert(x);


        }

      }
      
      void insert (Node* x){
        x->next = head->next;
        x->prev = head;
        head->next->prev = x;
        head->next = x;


      }
      void remove(Node* x){

        x->prev->next = x->next;
        x->next->prev = x->prev;

      }
  };
  
  /**
   * Your LRUCache object will be instantiated and called as such:
   * LRUCache* obj = new LRUCache(capacity);
   * int param_1 = obj->get(key);
   * obj->put(key,value);
   */