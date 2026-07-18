# Jenkins Multibranch Pipeline Practice

This is a small, dependency-free Python repository for practicing Jenkins
Multibranch Pipelines. Jenkins discovers every branch containing a
`Jenkinsfile`, runs its tests, and applies branch-specific pipeline stages.

## Branches

| Branch | Purpose | Expected pipeline behavior |
| --- | --- | --- |
| `main` | Production-ready code | Test, package, and deploy simulation |
| `develop` | Integration work | Test and package |
| `feature/friendly-greeting` | Example feature | Test only |

## Run locally

Python 3.9 or newer is sufficient; there are no external packages to install.

```powershell
python app.py "Your Name"
python -m unittest discover -s tests -p "test_*.py" -v
python package_app.py
```

On Linux or macOS, use `python3` in place of `python` if needed.

## Connect it to Jenkins

1. Create an empty repository in GitHub, GitLab, or Bitbucket.
2. Add it as a remote and push all branches:

   ```bash
   git remote add origin <repository-url>
   git push -u origin --all
   ```

3. In Jenkins, select **New Item**, choose **Multibranch Pipeline**, and enter
   the repository URL under **Branch Sources**.
4. Keep **Script Path** set to `Jenkinsfile`, save, and select **Scan
   Multibranch Pipeline Now**.
5. Open each discovered branch and compare which stages ran.

The Jenkins agent needs Git and Python 3. No Python dependencies or plugins
beyond normal Pipeline and source-control support are required.

## Practice exercises

1. Change the greeting on `feature/friendly-greeting`, commit, and push it.
2. Intentionally break its test and inspect the failed Jenkins build.
3. Merge the feature branch into `develop`; confirm that packaging now runs.
4. Merge `develop` into `main`; confirm that the deployment simulation runs.
5. Add a `when { changeRequest() }` stage and open a pull request.
6. Configure an orphaned-item strategy in Jenkins, delete a remote branch, and
   observe how its Jenkins job is cleaned up.

