# 01-jan-2021

### 3 - sort letter vs count letter prehash

https://sahandsaba.com/interview-question-grouping-words-into-anagrams.html

```python
import collections

def sort_prehash(word):
    return ''.join(sorted(word))


def count_letters_prehash(word):
    return tuple(collections.Counter(word).items())


def group_anagrams(words, hash_function):
    result = {}
    for w in words:
        s = hash_function(w.lower())
        if s in result:
            result[s] |= {w}
        else:
            result[s] = {w}
    return result.values()

# Usage:
>>> group_anagrams(['tsar', 'rat', 'tar', 'star', 'tars', 'cheese'], sort_prehash)
[set(['tars', 'tsar', 'star']), set(['cheese']), set(['rat', 'tar'])]
>>> group_anagrams(['tsar', 'rat', 'tar', 'star', 'tars', 'cheese'], count_letters_prehash)
[set(['tars', 'tsar', 'star']), set(['cheese']), set(['rat', 'tar'])]
```

### 2 - fast inverse square root

http://h14s.p5r.org/2012/09/0x5f3759df.html

```c
float FastInvSqrt(float x) {
  float xhalf = 0.5f * x;
  int i = *(int*)&x;         // evil floating point bit level hacking
  i = 0x5f3759df - (i >> 1);  // what the fuck?
  x = *(float*)&i;
  x = x*(1.5f-(xhalf*x*x));
  return x;
}
```

### 1 - overlayfs

https://en.wikipedia.org/wiki/OverlayFS

- OverlayFS is a union mount filesystem implementation for Linux. It combines multiple different underlying mount points into one, resulting in single directory structure that contains underlying files and sub-directories from all sources. Common applications overlay a read/write partition over a read-only partition, such as with LiveCDs and IoT devices with limited flash memory write cycles.

- The main mechanics of OverlayFS relate to the merging of directory access when both filesystems present a directory for the same name. Otherwise, OverlayFS presents the object, if any, yielded by one or the other, with the "upper" filesystem taking precedence. Unlike some other overlay filesystems, the directory subtrees being merged by OverlayFS do not necessarily have to be from distinct filesystems.[8]

- OverlayFS supports whiteouts and opaque directories in the upper filesystem to allow file and directory deletion.[8]

- OverlayFS does not support renaming files without performing a full copy-up of the file; however, renaming directories in an upper filesystem has limited support.

- OverlayFS does not support merging changes from an upper filesystem to a lower filesystem.


https://askubuntu.com/questions/109413/how-do-i-use-overlayfs

```
# Create the filesystems.
dd if=/dev/zero of=lower.ext4 bs=1024 count=102400
mkfs -t ext4 lower.ext4
cp lower.ext4 upper.ext4
mkdir lower upper overlay
sudo mount lower.ext4 lower
sudo mount upper.ext4 upper
sudo chown "$USER:$USER" lower upper
printf lower-content > lower/lower-file
# Upper and work must be on the same filesystem.
mkdir upper/upper upper/work
printf upper-content > upper/upper/upper-file
# Work must be empty. E.g. this would be bad:
#printf work-content > upper/work/work-file
# Make the lower readonly to show that that is possible:
# writes actually end up on the upper filesystem.
sudo mount -o remount,ro lower.ext4 lower

# Create the overlay mount.
sudo mount \
  -t overlay \
  -o lowerdir=lower,upperdir=upper/upper,workdir=upper/work \
  none \
  overlay \
;

# Interact with the mount.
printf 'overlay-content' > overlay/overlay-file
ls lower upper/upper upper/work overlay

# Write to underlying directories while mounted
# gives undefined behaviour.
#printf lower-content-2 > lower/lower-file-2
#printf upper-content-2 > upper/upper-file-2

# Unmount the overlay and observe state.
sudo umount overlay
ls lower upper/upper upper/work

# Cleanup.
sudo umount upper lower
```
