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
    unordered_map<int, Node*> cache; // Map for fast access
    Node* head; // Dummy head
    Node* tail; // Dummy tail

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        cache.reserve(capacity);

        // Initialize dummy head and tail for easy deletion/insertion
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1;
        }
        Node* node = cache[key];

        // Move node to front since it is recently used
        remove(node);
        insert(node);

        return node->value;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            // If key exists, update value and move to front
            Node* node = cache[key];
            node->value = value;
            remove(node);
            insert(node);
        } else {
            if (cache.size() == capacity) {
                // Remove least recently used node
                Node* lru = tail->prev;
                cache.erase(lru->key);
                remove(lru);
                delete lru;
            }
            // Insert new node at front
            Node* newNode = new Node(key, value);
            cache[key] = newNode;
            insert(newNode);
        }
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

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
