#include <iostream>
#include <unordered_map>

using namespace std;
class Node {

public:
  int key;
  int value;
  Node *prev;
  Node *next;

  Node(int key, int value) {
    this->key = key;
    this->value = value;
    this->prev = nullptr;
    this->next = nullptr;
  }
};

class LRUCache {

private:
  int capacity;
  unordered_map<int, Node *> cache;
  Node *head;
  Node *tail;

public:
  LRUCache(int capacity) {
    this->capacity = capacity;
    cache.reserve(capacity);
    head = new Node(0, 0);
    tail = new Node(0, 0);
    head->next = tail;
    tail->prev = head;
  }

  int get(int key) {

    // check if the value exists first:

    if (cache.find(key) == cache.end()){
        return -1;
    } 
        Node* resnode = cache[key];
        remove(resnode);
        insert(resnode);
        return resnode->value;
        
    



  }

  void put(int key, int value) {

    // check first if key already exists:
    if (cache.find(key) != cache.end()) {

      Node *temp = cache[key];
      temp->value = value;
      remove(temp);
      insert(temp);


    }
    // check capacity:
    else {
      if (cache.size() == this->capacity) {
        // last item is
        Node *last_node = tail->prev; // this is the last node
        cache.erase(last_node->key);
        remove(last_node);
      }
      Node* new_node = new Node(key,value);
      cache[key] = new_node;
      insert(new_node);

    }
    //
  }

private:
  void remove(Node* node) {

    node->prev->next = node->next;
    node->next->prev = node->prev;


  }

  void insert(Node* node) {

      node->next = head->next;
      node->prev = head;
      head->next->prev = node;
    head->next = node;



  }
};
