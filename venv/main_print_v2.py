# pip install rich 가 필요합니다.
from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

# 변수 선언
name = "Alice"
age = 25
score = 95.5
data = {"name": name, "age": age, "score": score}

# 1) 컬러 문자열 출력 (f-string)
rprint(f"[bold green]Hello, {name}![/bold green] Your score is [cyan]{score:.2f}[/cyan].")

# 2) 패널(박스) 형태로 출력
panel_text = f"""
[bold]Student Info[/bold]
- Name : [yellow]{name}[/yellow]
- Age  : [magenta]{age}[/magenta]
- Score: [cyan]{score:.2f}[/cyan]
"""
rprint(Panel(panel_text, title="Profile", border_style="blue"))

# 3) 테이블 출력 (딕셔너리/리스트 같이 출력)
table = Table(title="Records")
table.add_column("Key", style="bold")
table.add_column("Value")

for k, v in data.items():
    table.add_row(k, str(v))

rprint(table)

# 4) sep, end 옵션 (rich.print 도 기본 print 옵션 동일)
rprint("2025", "09", "23", sep="-", end="\n\n")
