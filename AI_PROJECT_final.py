{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# These relationships are specified in a file called relationships.json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'logpy'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-076bcffbb621>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mjson\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mlogpy\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mRelation\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfacts\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrun\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mconde\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvar\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0meq\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'logpy'"
     ]
    }
   ],
   "source": [
    "import json \n",
    "from logpy import Relation, facts, run, conde, var, eq \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#WE MADE a function to check if x is the parent of y\n",
    " \n",
    "def parent(x, y): \n",
    "    return conde([father(x, y)], [mother(x, y)]) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#CREATING a function to check if x is the grandparent of y. \n",
    "# the logic is simple that if x is the grandparent of y, then the offsprings of x will be the parent of y\n",
    "# Check if 'x' is the grandparent of 'y' \n",
    "def grandparent(x, y): \n",
    "    temp = var() \n",
    "    return conde((parent(x, temp), parent(temp, y))) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check for sibling relationship between 'a' and 'b'   \n",
    "def sibling(x, y): \n",
    "    temp = var() \n",
    "    return conde((parent(temp, x), parent(temp, y))) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Relation' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-dd022f5a0da2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m\u001b[1;33m==\u001b[0m\u001b[1;34m'__main__'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m     \u001b[0mfather\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mRelation\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m     \u001b[0mmother\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mRelation\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Relation' is not defined"
     ]
    }
   ],
   "source": [
    "if __name__=='__main__': \n",
    "    father = Relation() \n",
    "    mother = Relation() \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'famtree.json'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-fe309b759008>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'famtree.json'\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m     \u001b[0md\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mjson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mloads\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'famtree.json'"
     ]
    }
   ],
   "source": [
    "    with open('famtree.json') as f: \n",
    "        d = json.loads(f.read()) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "    for item in d['father']: \n",
    "        facts(father, (list(item.keys())[0], list(item.values())[0])) \n",
    " \n",
    "    for item in d['mother']: \n",
    "        facts(mother, (list(item.keys())[0], list(item.values())[0])) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "  x = var() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "    #  children of pandu \n",
    "    name = 'pandu' \n",
    "    output = run(0, x, father(name, x)) \n",
    "    print(\"\\nList of \" + name + \"'s children:\") \n",
    "    for item in output: \n",
    "        print(item) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "    # arjunas mother \n",
    "    name = 'arjuna' \n",
    "    output = run(0, x, mother(x, name))[0] \n",
    "    print(\"\\n\" + name + \"'s mother:\\n\" + output) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "    # yudistiras parent parents  \n",
    "    name = 'yudistira' \n",
    "    output = run(0, x, parent(x, name)) \n",
    "    print(\"\\nList of \" + name + \"'s parents:\") \n",
    "    for item in output: \n",
    "        print(item) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "    # gatog grandparents  \n",
    "    name = 'gatog' \n",
    "    output = run(0, x, grandparent(x, name)) \n",
    "    print(\"\\nList of \" + name + \"'s grandparents:\") \n",
    "    for item in output: \n",
    "        print(item) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "    # kunti grandchildren  \n",
    "    name = 'kunti' \n",
    "    output = run(0, x, grandparent(name, x)) \n",
    "    print(\"\\nList of \" + name + \"'s grandchildren:\") \n",
    "    for item in output: \n",
    "        print(item) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "    # bhima siblings  \n",
    "    name = 'bhima' \n",
    "    output = run(0, x, sibling(x, name)) \n",
    "    siblings = [x for x in output if x != name] \n",
    "    print(\"\\nList of \" + name + \"'s siblings:\") \n",
    "    for item in siblings: \n",
    "        print(item) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " # sutasoma uncles \n",
    "    name = 'sutasoma' \n",
    "    name_father = run(0, x, father(x, name))[0] \n",
    "    output = run(0, x, uncle(x, name)) \n",
    "    output = [x for x in output if x != name_father] \n",
    "    print(\"\\nList of \" + name + \"'s uncles:\") \n",
    "    for item in output: \n",
    "        print(item) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "    # All wives\n",
    "    a, b, c = var(), var(), var() \n",
    "    output = run(0, (a, b), (father, a, c), (mother, b, c)) \n",
    "    print(\"\\nList of all spouses:\") \n",
    "    for item in output: \n",
    "        print('Husband:', item[0], '<==> Wife:', item[1]) \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
