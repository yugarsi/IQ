'''
final state: [[1, 2, 3].  0 1,3
                          1 0,2,4
                          2 1,5
                          3
              [4, 5, 0]]

              [1 2 3 4 5 0]


 2x3 -> 2d grid [1 2 3 4 5 0]


 input1 = [[3, 2, 5]
           [0, 1, 4]]
           [[3, 2, 5],
           [1, 0, 4]]
           [[3, 2, 5],
           [1, 4, 0]]

           [[3, 2, 0],
           [1, 4, 5]]

           [[3, 0, 2],
           [1, 4, 5]]

           [[0, 3, 2],
           [1, 4, 5]]
           [[1, 3, 2],
           [0, 4, 5]]

           [[1, 3, 2],
           [4, 0, 5]]

           [[1, 3, 2],
           [4, 5, 0]]


input2 = [[1, 2, 3]
          [4, 0, 5]]

          [[1, 2, 3]
          [4, 5, 0]]

minimum number of moves (up, down, left, right)

-1 -> if not
minimum moves -> should be answer
'''

input2 = [[1, 2, 3]
          [4, 0, 5]]


def ifpossible(input):
    final_state = [[1, 2, 3]
                   [4, 5, 0]];

    for i in fina
        finalset =
    for i in range(len(input))

    queue = []

    private
    final
    int[]
    final = {1, 2, 3, 4, 5, 0};

    private
    int
    minMoves(int[][]
    grid) {

        int[]
    g = convert(grid);

    if (Arrays.equals(g, final)) {
    return 0;
    }

    Set < int[] > set = new
    HashSet <> ();
    Queue < Pair < int[], Integer >> queue = new
    LinkedList <> ();
    queue.add(new
    Pair(g, 0));
    set.add(g);

    while (!queue.isEmpty()) {

    Pair < int[], Integer > current = queue.poll();

    if (reached(current.getKey(), this.final)) {
    return current.getValue();
    }
    List < int[] > list = getNextStates(current.getKey());
    for (int[] arr: list) {
        if (!set.contains(arr)) {
        queue.add(new Pair(arr, current.getValue() + 1));
        set.add(arr);
        }
    }
    }
    return -1;

}

private
boolean
reached(int[]
arr, int[]
final) {
return Arrays.equals(arr, final);
}

private
List < int[] > getNextStates(int[]
arr) {

int
index = 0;
for (int i = 0; i < arr.length; i++) {
if (arr[i] == 0){
index = i;
}
}

List < int[] > result = new
ArrayList <> ();

}






