# -*- coding: utf-8 -*-

import os

def create_md_files(filenames):
    for filename in filenames:
        file_with_extension = "{}.md".format(filename)
        
        with open(file_with_extension, 'w') as f:
            f.write("# {}\n\n".format(filename))
        
        print("Created file: {}".format(file_with_extension))

filenames = [
"00_9-铂金VIP的介绍"

]

create_md_files(filenames)
