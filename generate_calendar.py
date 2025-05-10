import os
import argparse
from datetime import datetime, timedelta

def generate_calendar_html(year: int, month: int):
    output_dir = str(year)
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{str(year)[2:]}-{str(month).zfill(2)}.html"
    filepath = os.path.join(output_dir, filename)

    first_day = datetime(year, month, 1)
    last_day = (first_day.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>{year}年{str(month).zfill(2)}月カレンダー</title>
<style>
  body {{ font-family: sans-serif; margin: 20px; }}
  table {{ border-collapse: collapse; width: 100%; }}
  td {{ border: 1px solid #ccc; width: 20%; height: 100px; vertical-align: top; padding: 5px; }}
  .date-label {{ font-weight: bold; margin-bottom: 5px; }}
  textarea {{ width: 100%; height: 60px; resize: none; }}
  button {{ margin: 10px 0; }}
</style>
</head>
<body>
<h2>{year}年{str(month).zfill(2)}月</h2>
<button onclick="overwriteCalendar()">上書き保存</button>
<div id="calendar">
<table>
"""

    start_date = first_day - timedelta(days=first_day.weekday())
    current = start_date

    while current <= last_day or current.weekday() != 0:
        html += "<tr>\n"
        for i in range(7):
            if current.month == month and current.weekday() < 5:
                label = f"{current.month}/{current.day}"
                html += f'<td><div class="date-label">{label}</div><textarea></textarea></td>\n'
            else:
                html += "<td></td>\n"
            current += timedelta(days=1)
        html += "</tr>\n"

    html += """</table>
</div>
<script>
let isModified = false;

function bindTextareaEvents() {
  document.querySelectorAll("textarea").forEach(textarea => {
    textarea.addEventListener("input", () => {
      isModified = true;
    });
  });
}

window.addEventListener("DOMContentLoaded", () => {
  bindTextareaEvents();
});

window.onbeforeunload = function () {
  if (isModified) {
    return "変更内容が保存されていない可能性があります。";
  }
};

function overwriteCalendar() {
  const calendar = document.getElementById("calendar");

  calendar.querySelectorAll("textarea").forEach(textarea => {
    const parent = textarea.parentNode;
    const label = parent.querySelector(".date-label").outerHTML;
    const value = textarea.value.replace(/</g, "&lt;").replace(/>/g, "&gt;");
    const newTextarea = `<textarea>${value}</textarea>`;
    parent.innerHTML = label + newTextarea;
  });

  const html = document.documentElement.outerHTML;
  const blob = new Blob([html], { type: "text/html" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);

  const currentFile = window.location.pathname.split('/').pop() || "calendar.html";
  a.download = currentFile;
  a.click();

  isModified = false;
  bindTextareaEvents();  // ← 新しく生成された textarea にイベント再付与
}
</script>

</body>
</html>"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ カレンダーを生成しました: {filepath}")

# コマンドライン引数対応
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTMLカレンダーを生成")
    parser.add_argument("-y", "--year", type=int, required=True, help="生成する年（例: 2025）")
    parser.add_argument("-m", "--month", type=int, required=True, help="生成する月（例: 5）")
    args = parser.parse_args()
    generate_calendar_html(args.year, args.month)

