import  os
os.environ["PATH"] = "C:\\tools\\PortableGit-2.35.1.2-64-bit\\bin;%PATH%"

import git
gitrepo = "C:\\__myRepo__\\GitHub\\celilaktas\\gitchangelog"
#gitrepo = "c:\\path-to-git-repo"

def get_tag_info(repo, tagname):
    return repo.git.execute(f"git tag -n {tagname}")[16:]
    
def main():
    global gitrepo
        
    repo = git.Repo(gitrepo)
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)

    for i, tag in enumerate(tags):
        tagname = tags[-i-1]
        commitsha = tags[-i-1].commit.hexsha
        print(f"\n{tagname} {get_tag_info(repo, tagname)} ({tags[-i-1].commit.committed_datetime.date()})")    
        print("=========")
        print(f"{tags[-i-1].commit.message}")
        if i<(len(tags)-1):
            cmd = f"git log {tags[-i-2]}..{tags[-i-1]} --oneline"
        else:
            cmd = f"git log {tags[0]} --oneline"
        log = repo.git.execute(cmd)
        print(log)
        
if __name__ == '__main__':
    main()    