#include <iostream>
#include <unordered_map>
using namespace std;
class Node {
  public:
  Node* prev;
  Node* next;
  int key;
  int value;
  Node(int key, int value){
    this->key = key;
    this->value = value;
    this->prev = nullptr;
    this->next = nullptr;
  };
};

class LRUCache {
  public:
  Node* head;
  Node* tail;
  unordered_map<int, Node*> cache;
  int capacity;
  
      LRUCache(int capacity) {
        this->capacity = capacity;
        this->head = new Node(0,0);
        this->tail = new Node(0,0);

        this->head->next = tail;
        this->tail->prev = head;

          
      }
      
      int get(int key) {

        // check if key is in 
        
        if(cache.find(key) != cache.end()){
          Node* resnode = cache[key];

          remove(resnode);
          add(resnode);

          return cache[key]->value;

        }
        
        return -1;
      }
      
      void put(int key, int value) {
        // check size first:
        if (cache.find(key) != cache.end()){
            Node* lastnode = cache[key];
            remove(lastnode);
            cache.erase(lastnode->key);
            delete lastnode;
            
          }
        else if (cache.size() == capacity){
          // remove the last node
          Node* lastnode = tail->prev;
          remove(lastnode);
          cache.erase(lastnode->key);
          delete lastnode;
        }

          Node* new_node = new Node(key,value);
          add(new_node);
          cache[key] = new_node;
          return;

          
      }
      void add(Node* node){
        node->next = this->head->next;
        node->prev = this->head;
        
        this->head->next->prev = node;
        this->head->next = node;
        

      }
      void remove(Node* node){
        node->next->prev = node->prev;
        node->prev->next = node->next;
      }
  };
  
  /**
   * Your LRUCache object will be instantiated and called as such:
   * LRUCache* obj = new LRUCache(capacity);
   * int param_1 = obj->get(key);
   * obj->put(key,value);
   */