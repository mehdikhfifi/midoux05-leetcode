
#include <iostream>

#include <unordered_map>

using namespace std;




class Node {

  public:

  int key;
  int value;
  Node* prev;
  Node* next;


  Node(int key, int value){
    this->key = key;
    this->value = value;
    prev = nullptr;
    next = nullptr;
  }

};


class LRUCache {
  public:


  unordered_map<int, Node*> cache;
  Node* tail;
  Node* head;
  int capacity;
// node does not have a default constructor

      LRUCache(int capacity) {

        this->tail = new Node(0,0);
        this->head = new Node(0,0);
        this->head->next = tail;
        this->tail->prev = head;
        this->capacity = capacity;
      }
      
      int get(int key) {

        // check if key is inside the lru first

        if (cache.find(key) == cache.end()){
          return -1;
        }
        else{
          Node* res = cache[key];

          this->remove(res);
          this->add(res);

          return res->value;

        }
          
      }
      
      void put(int key, int value) {

        // check capacity first;


        if (cache.find(key) != cache.end()){
         // check if the item is already inside the list
         
         // remove it first before readding

         Node* res_item = cache[key];

         remove(res_item);

         cache.erase(key);

         delete (res_item);

         }
        else if (cache.size() == capacity){

          // remove last item

          Node* last_item = tail->prev;
          
          remove(last_item);
          
          this->cache.erase(last_item->key);
          
          delete (last_item);
        } 


          Node* new_node = new Node(key,value);

          add(new_node);

          this->cache[key] = new_node;
          
      }


      void add (Node* node){

        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;

      }
      void remove( Node* node){
        node->prev->next = node->next;
        node->next->prev = node->prev;
      }
  };
  
  /**
   * Your LRUCache object will be instantiated and called as such:
   * LRUCache* obj = new LRUCache(capacity);
   * int param_1 = obj->get(key);
   * obj->put(key,value);
   */