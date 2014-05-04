# phylesystem

This is the top-level repository in the Open Tree of Life
phylogenetic study document store.
The data are actually stored in different repositories referred
to as ``shards'' in much of our documentation/email discussions.

Phylesystem serves as a crude database storage for the 
web services implemented using the code base
[api.opentreeoflife.org](https://github.com/OpenTreeOfLife/api.opentreeoflife.org).
This layer is often referred to as "the API" (though a better name 
would probably be "NexSON services API")

Currently we do not support pull requests to the shards.
The server running the NexSON services API is the only 
writer. We hope to add functionality to smoothly deal
with pull requests soon.



# Usage

Most users will only want/need to run the 

    $ bash pull-studies.bash

script to fetch and pull the latest NexSON for all of the shards





# History

The repository formerly known as phylesystem was moved to:
https://github.com/mtholder/old-phylesystem
before the current architecture was decided.
That repository has a set of files that agree with the intial commit to the
phylesystem-1 repo; and it had scripts for updating from phylografter

## License

The *code* in this repository is released under the 2-clause BSD license. See
the LICENSE file for more details.

The *data* in this repository is released under the [Create Commons Zero 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) license.

