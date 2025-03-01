
#include <iostream>
#include <unordered_map>

using namespace std;

class Node {
public:
    int key;
    int value;
    Node* prev;
    Node* next;
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
    unordered_map<int, Node*> cache;
    Node* head;
    Node* tail;

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

        if (cache.find(key) == cache.end()) {
            return -1;
        }

        Node* temp = cache[key];

        remove(temp);
        insert(temp);

        return temp->value;
    }

    void put(int key, int value) {

        // check if it exists already

        if (cache.find(key) != cache.end()) {

            Node* node = cache[key];
            node->value = value;
            remove(node);
            insert(node);

        } else {
            if (cache.size() == capacity) {
                Node* lru = tail->prev;

                cache.erase(lru->key);
                remove(lru);
                delete lru;
            }
        // youcan now insert it
        Node* newnode = new Node(key, value);
        cache[key] = newnode; // ??????? wtf is going on
        insert(newnode);
        }
    }

    // helper functions
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

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */