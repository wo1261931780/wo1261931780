#!/usr/bin/env python3
import subprocess
import os

os.chdir('/Users/liujiajun/Documents/GitHub/wo1261931780')

# Complete the merge
subprocess.run(['git', 'commit', '-m', 'Merge remote-tracking branch origin/main: 合并远程Profile卡片更新(UTC+8时区修正),保留本地Profile内容优化'], check=True)

# Push to remote
result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
print("Push完成!")
print(result.stdout)
if result.stderr:
    print(result.stderr)
