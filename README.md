# pytest_ci_learn

一个用于学习 pytest + GitHub Actions CI 的示例项目。包含 pytest 测试、覆盖率、flake8 lint、Allure 测试报告（部署到 GitHub Pages）以及 Docker 镜像构建。

![CI](https://github.com/Lawwaikit/pytest_ci_learn/actions/workflows/ci.yml/badge.svg)

- 在线测试报告（Allure）：https://lawwaikit.github.io/pytest_ci_learn/
- 每次推送到 main 后自动重新生成报告

## 项目结构

```
pytest_ci_learn/
├── app/
│   └── calculator.py         # 被测代码：add / sub
├── testcases/
│   ├── conftest.py           # fixture + hook 演示
│   ├── test_calculator.py    # 参数化 + marker + allure
│   ├── test_api.py
│   ├── test_user.py
│   └── test_33.py            # indirect 参数化
├── .github/workflows/ci.yml  # GitHub Actions CI
├── pytest.ini                # pytest 配置（addopts=-vs, markers 等）
├── pyproject.toml            # 打包配置（packages.find = app）
├── requirements.txt
├── main.py                   # CLI 入口
└── dockerfile
```

## 本地运行

### 准备环境

```powershell
uv venv
uv pip install -r requirements.txt
.venv\Scripts\Activate.ps1
```

### 跑测试

```powershell
pytest                                  # 全量跑（读 pytest.ini，默认 -vs）
pytest -m smoke                         # 只跑 smoke 标记
pytest testcases/test_calculator.py     # 只跑某文件
pytest -n auto                          # 并行跑（pytest-xdist）
pytest --reruns 2                       # 失败重跑（pytest-rerunfailures）
pytest --cov=app --cov-report=term      # 覆盖率（pytest-cov）
pytest --html=report.html --self-contained-html   # HTML 报告（pytest-html）
pytest --alluredir=allure-results       # 生成 allure 数据（allure-pytest）
```

### 跑 CLI

```powershell
python main.py add 2 3    # Result: 5
python main.py sub 10 4  # Result: 6
```

## CI（GitHub Actions）

工作流 `.github/workflows/ci.yml` 在 push 到 main 或开 PR 时触发，包含：

| job | 作用 | 触发 |
|---|---|---|
| `test-lint-coverage` | pytest + 覆盖率 + flake8 + 测试结果回写 + 产物上传 | push / PR |
| `deploy-report` | 生成 Allure 报告并部署到 GitHub Pages | push 到 main |
| `docker-build-push` | 构建 Docker 镜像并推送到 Docker Hub | 打 tag（v*） |

特性：
- pip 缓存（`cache: pip`）加速依赖安装
- `concurrency` 取消旧的重复 run
- `dorny/test-reporter` 把用例通过/失败回写到 PR
- 测试报告产物（pytest-html / coverage html / junit / allure 数据）在 run 页面 Artifacts 可下载
- Allure 报告部署到 GitHub Pages，浏览器在线查看，无需下载

## 分支保护

`main` 分支已启用保护：
- 必须通过 PR 合并（不能直接 push 到 main）
- CI（`test-lint-coverage`）必须通过才能合并

## Docker 镜像发布

打 tag 触发 `docker-build-push`。需先在仓库 Settings -> Secrets and variables -> Actions 配置：
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

```powershell
git tag v0.1.0
git push origin v0.1.0
```