extern "C" {
  extern void run(int input);
}

#include "nbind/nbind.h"

NBIND_GLOBAL() {
  function(run);
}
