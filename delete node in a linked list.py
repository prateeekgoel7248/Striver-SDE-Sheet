void DeleteLast() {
  if (head == nullptr)
    cout << "There are no nodes to delete in LinkedList" << endl;

  // If there is single node, delete that and make head point to null
  if (head -> next == nullptr) {
    delete head;
    head = nullptr;
  } else {

    // step1: Finding First and Second Last Node in LinkedList

    ListNode * curr = head, * prev = nullptr;
    while (curr -> next != nullptr) {
      prev = curr;
      curr = curr -> next;
    }

    // Step2 : Pointing prev->next to nullptr

    prev -> next = nullptr;

    // Step3 :Deleting the LastNode

    delete curr;
  }
}
