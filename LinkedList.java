

public class LinkedList {
    public static class Node {

        Node next;
        String data;

        public Node(String data) {
            this.data = data;
        }

    }

    Node head;

    public void addFirst(String data) {
        if(head == null) {
            head = new Node(data);
            return;
        }
        Node newHead = new Node(data);
        newHead.next = head;
        head = newHead;
    }

    public void addLast(String data) {
        if(head == null) {
            head = new Node(data);
            return;
        }
        Node current = head;
        while(current.next != null) {
            current = current.next;
        }
        current.next = new Node(data);
    }

    public void removeFirst() {
        if(head == null) {
            return;
        }
        head = head.next;
    }

    public void removeLast() {
        if(head == null) {
            return;
        }
        if(head.next == null) {
            head = null;
            return;
        }
        Node current = head;
        Node previous = null;
        while(current.next != null) {
            previous = current;
        }
        current = current.next;
        previous.next = null;
    }

    public void removeValue(String data) {
        if(head == null) {
            return;
        }
        if(head.data.equals(data)) {
            head = head.next;
            return;
        }
        Node current = head;
        while(current.next != null) {
            if(current.next.data.equals(data)) {
                current.next = current.next.next;
                return;
            }
            current = current.next;
        }
    }
}

