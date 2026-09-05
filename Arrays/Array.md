Array - `fixed size data structure`, and is used to store `values` of the `same type`.
It is an `ordered` data structure, it is one of the most important properties of the array.

By being `ordered`, array allows `efficient element access` via `subscription - []`.
It is O(1) time to retrieve a particular element from the array. That is why it is efficient.

Why is it O(1) time you may ask. Well that is because, the data structure `tracks` its `first` element's actual
memory address in RAM, and then for `each additional element` it keeps `allocating` a `fixed` amount of memory.

Example: nums = [1, 2, 3]

So, in RAM, the program allocates some space let's say the Ox1000 for the first element.
And each additional element would be getting plus the size of the each element of the array.

For example if each number takes 4 bytes, then: the second element is gonna be 0x1004 memory address.
The third is gonna be at 0x1008, and so on, so forth.