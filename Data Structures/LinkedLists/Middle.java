//modified code
import java.util.*;

class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Linked {
    Node head;

    Linked() {
        head = null;
    }

    void insertAtEnd(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }

    void middleElement() {
        if (head == null) {
            System.out.println("The list is empty.");
            return;
        }

        Node slow = head;
        Node fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        System.out.println("The middle element is: " + slow.data);
    }
}

public class Middle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Linked ll = new Linked();
        
        System.out.println("Enter the number of elements in the linked list:");
        int size = sc.nextInt();

        for (int i = 0; i < size; i++) {
            System.out.println("Enter element " + (i + 1) + ":");
            int data = sc.nextInt();
            ll.insertAtEnd(data);
        }

        ll.middleElement();
        
        // Close the scanner
        sc.close();
    }
}

