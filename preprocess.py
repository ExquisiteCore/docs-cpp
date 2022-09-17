"""!@package preprocess
@author Futrime (futrime@outlook.com)
@brief The preprocessor for LiteLoaderSDK documentation
@version 1.0.0
@date 2022-08-28

@details This program preprocess the LiteLoaderSDK for Doxygen documentation
         generation, removing all Doxygen comment blocks with \c \@symbol but
         without \c \@brief in header files in the SDK.

@copyright Copyright (c) 2022 Futrime
"""

"""
    LiteLoaderBDS C++ Documentation Preprocessor, a preprocessor for
    the C++ documentation of LiteLoaderBDS.
    Copyright (C) 2022  Futrime

    This program is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this program.  If not, see
    <https://www.gnu.org/licenses/>.
"""


import os
import re

regex_list = [
    ' *\/\*{2}\n( +\* @hash.*\n| +\* @symbol.*\n| +\* @vftbl.*\n)* +\*\/\n', # comments before methods
    ' *\/\*\*\n * \* @brief MC \w+ \w+\.\n * \*\n * \*\/\n' # comments before classes
]

if __name__ == '__main__':
    file_list = []

    for root, dirs, files in os.walk('./SDK/Header/MC/'):
        for file_name in files:
            file_list.append(os.path.join(root, file_name))

    for file_path in file_list:
        print('Preprocessing ' + file_path)

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        for regex in regex_list:
            content = re.sub(regex, '', content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)