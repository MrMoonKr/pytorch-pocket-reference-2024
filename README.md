# 책 부록 소스 프로젝트 입니다

직무 교육( OJT, On the job Training )을 위해서 클론 하였습니다.  


## 책 관련 링크  

- [PyTorch Pocket Reference [ 원서 ]](https://www.oreilly.com/library/view/pytorch-pocket-reference/9781492089995/)  

- [PyTorch Pocket Reference [ 국내 ]](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=263192314)  


## 개발 및 테스트 환경

- windows 11  
- NVIDIA RTX 2030 10G
- [cuda_12.1.0_531.14_windows.exe](https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda_12.1.0_531.14_windows.exe)
- nvidia-smi.exe ( NVIDIA-SMI 536.23 CUDA Version: 12.2 )
- Python 3.10.11
- pip 23.0.1
- venv  
- VS Code  
- ...  

  ```
  // PowerShell
  $ Get-ExecutionPolicy
  $ Set-ExecutionPolicy -Scope CurrentUser Unrestricted
  $ Get-ExecutionPolicy
  ```
  ```
  // PowerShell
  $ python -m venv .venv-local
  $ .venv-local/Scripts/Activate.ps1 
  $ (.venv-local) python --version
  $ (.venv-local) pip --version
  $ (.venv-local) pip list
  ```
  ```
  // PowerShell
  $ (.venv-local) pip install ipykernel
  $ (.venv-local) pip freeze > requirements.txt
  ```
  ```
  // PowerShell
  $ (.venv-local) pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121  
  $ (.venv-local) pip freeze > requirements.txt
  ```
  ```
  // PowerShell
  $ (.venv-local) pip install -r requirements.txt
  ```

## 사전 지식

- https://pytorch.org/get-started/locally/
- Python  
- pip  
- venv  
- jypyter notebook  
- ...  

---
---
---


# PyTorch Pocket Reference Code
Code included in the book, PyTorch Pocket Reference

![Book](https://raw.githubusercontent.com/joe-papa/pytorch-book/main/files/pytorch-book-cover.jpg)

[Available on Amazon](http://pytorchbook.com)
