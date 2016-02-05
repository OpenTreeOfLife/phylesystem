# phylesystem

This is the top-level repository in the Open Tree of Life
phylogenetic study document store.
The data are actually stored in different repositories referred
to as "shards" in much of our documentation/email discussions.

If you want to browse the data in phylesystem, you can
look at the repository for the only shard. The repo is at https://github.com/OpenTreeOfLife/phylesystem-1
If you want to find study `ot_WXYZ` you should look in `study/ot_YZ/ot_WXYZ/ot_WXYZ` (in other words, in the
study subdirectory look in the directory named using the study's prefix ("ot_" or "pg_") followed by the last 2 digits of the ID. In that directory there will be a subdirectory that corresponds to the study ID.
and the JSON file will be in that directory.

Phylesystem serves as a crude database storage for the 
web services implemented using the code base
[phylesystem-api](https://github.com/OpenTreeOfLife/phylesystem-api).
This layer is the API for accessing the NexSON data store. 

Currently we do not support pull requests to the shards.
The server running the NexSON services API is the only 
writer. We hope to add functionality to smoothly deal
with pull requests soon.

See [our publication on phylesystem](http://dx.doi.org/10.1093/bioinformatics/btv276) for details.

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

