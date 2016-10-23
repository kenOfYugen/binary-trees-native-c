# binary-trees-native-c

C binary trees benchmark ported from [the benchmark 
game](http://benchmarksgame.alioth.debian.org/u64q/program.php?test=binarytrees&lang=gcc&id=3) 
as a node.js addon.

## Install
`npm install kenOfYugen/binary-trees-native-c`

Tested on Arch Linux.

If it doesn't compile on your system, make sure that the dependencies specified 
in `binding.gyp` are met, and try again.

## Use

```javascript
var binaryTreesC = require('binary-trees-native-c');

binaryTreesC.run(10);
```
