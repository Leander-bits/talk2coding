# 上传与复用

文档由 AI 维护，上传动作需要你的明确授权。账号登录、创建凭证或网页上的确认可能仍需你操作，不需要手工修改 Markdown。

## 上传模板

在 GitHub 创建空仓库，不额外生成 README、许可证或 .gitignore。然后可以把下面的提示词交给 AI：

```text
请将当前模板上传到我的仓库：[准确仓库地址]，目标分支：[分支名]。
我授权检查本地状态、暂存并提交本次模板变更、配置该目标 remote，并推送到指定分支。
先检查两份规则一致、文档链接、差异和敏感信息；保留已有修改及历史。
已有 Git 仓库不要重复初始化，不覆盖未知 remote，不强制推送。
遇到需要我登录或操作网页的部分，说明具体步骤。
```

如需自行执行，在检查差异后使用以下 Git 命令；用实际地址替换占位内容。已存在的仓库或 remote 跳过对应步骤。

```powershell
git init -b main
git status --short
git add .
git diff --cached
git commit -m "chore: update agentic coding template"
git remote add origin https://github.com/YOUR_USERNAME/agentic-coding-template.git
git remote -v
git push -u origin main
```

Git 提示缺少提交身份时，在本仓库设置实际姓名与提交邮箱。按认证提示登录，不把令牌放进命令、URL 或文件；远端不为空或 remote 已存在时先检查原因。

推送后在仓库 `Settings → General` 勾选 `Template repository`。在 `Actions` 查看规则一致性检查；若需要阻止未通过的合并，另行配置 rulesets 或分支保护。

## 用于新项目

推荐在模板仓库选择 `Use this template → Create a new repository`，再 clone 新项目：

```powershell
git clone https://github.com/YOUR_USERNAME/my-project.git
Set-Location my-project
git remote -v
```

也可直接 clone 模板到新目录，在该目录把 `origin` 改名为 `template`，为新项目创建空仓库，再添加新的 `origin`。这样保留模板历史；推送前核对目标，不删除 .git 或强制改写历史。

创建后从 [分步提示词](PROMPTS.md) 开始，让 AI 根据需求更新代码和文档。模板后续变更不会自动同步到已有项目。

操作依据见 [GitHub 官方本地上传指南](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)、[创建模板仓库](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)及[从模板创建仓库](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)。
