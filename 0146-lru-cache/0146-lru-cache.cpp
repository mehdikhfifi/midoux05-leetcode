#include <iostream>
#include <unordered_map>
using namespace std;
class Node{

  public:
  Node* prev;
  Node* next;
  int key;
  int value;

  Node(int key, int value){
    this->prev = nullptr;
    this->next = nullptr;
    this->key = key;
    this->value = value;
  }
};

class LRUCache {
  public:
  unordered_map<int, Node*> cache;
  int capacity;
  Node* head;
  Node* tail;
    
      LRUCache(int capacity) {
        this->capacity = capacity;
        this->head = new Node(0,0);
        this->tail = new Node(0,0);
        this->head->next = this->tail;
    this->tail->prev = this->head;

      }
      
      int get(int key) {
        // first check does it exist

        if (this->cache.find(key) != this->cache.end()){
          Node* resnode = this->cache[key];

          remove(resnode);
          insert(resnode);
          

          return resnode->value;
        }
        else{
          return -1;
        }
          
      }
      
      void put(int key, int value) {
          // check if its already there:

          if(this->cache.find(key)!= this->cache.end()){
          
            Node* resnode = this->cache[key];
            resnode->value = value;

            remove(resnode);
            insert(resnode);
          

          return;
          }
          else{
            if (this->cache.size() == this->capacity){

              // must remove last node

              Node* lastnode = tail->prev;
              this->cache.erase(lastnode->key);
              remove(lastnode);

            }
            Node* x = new Node(key,value);
            this->cache[key] = x;
            insert(x);
          }
      }

      void insert(Node* x ){
        x->next = head->next;
        x->prev = head;
        head->next->prev = x;
        head->next = x;
      }
      void remove(Node* y){
        y->prev->next = y->next;
        y->next->prev = y->prev;
      }
  };
  
  /**
   * Your LRUCache object will be instantiated and called as such:
   * LRUCache* obj = new LRUCache(capacity);
   * int param_1 = obj->get(key);
   * obj->put(key,value);
   */