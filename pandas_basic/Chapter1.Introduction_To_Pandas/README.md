# فصل 1. آشنایی با کتابخانه Pandas

کتابخانه Pandas، با تحلیل روی ابر داده ( Big Data )، امکان پالایش اطلاعات نام منظم، مدیریت اطلاعات و همچنین امکانات آماری در اختیار مهندسین داده کاوی قرار می دهد.

## نصب Pandas

1. برای نصب Pandas، باید نسخه pip بالاتر از pip>=19.3 باشد. برای مشاهده نسخه pip نصب شده روی سیستم، دستور ذیل در محیط ترمینال وارد کنید.

```bash
pip --version
```

![pip-check-version](img/pip-check-version.PNG)

در صورتیکه نسخه pip شما کمتر از 19.3 بود، از لینک مقابل آخرین نسخه پایتون نصب کنید. [دانلود پایتون](https://www.python.org/downloads/)

2. کتابخانه Pandas نصب می کنیم.

```bash
pip install pandas
```

3. برای اطمینان نصب Pandas، دستورات ذیل در محیط برنامه نویسی پایتون وارد می کنیم.

```python
import pandas as pd
print(pd.__version__)
```

📁 [مشاهده پروژه](project/1.check_pip_version.py)

## شروع برنامه نویسی

قصد داریم، نمرات دانشجویان به کمک کتابخانه Pandas، نمایش دهیم.

کتابخانه pandas به پروژه وارد می کنیم. ( معمولا از نام مستعار pd برای صدا زدن این کتابخانه استفاده می شود. )

```python
import pandas as pd
```

داده های کلاس در قالب Dictionary اضافه می کنیم.

> 💡 به مجموعه داده های آماری، که هدف تجزیه و تحلیل می باشند، Data Set گفته می شود.

```python
import pandas as pd

dataSet = {
    "Name": [
        "Arash",
        "Shahram",
        "Omid",
        "Morteza",
        "Najme",
        "Mahsa",
        "Elham",
        "Maryam",
        "Sanam",
    ],
    "Physic ": [15, 15.25, 18, 17, 8, 14, 18, 17, 13],
    "chemistry": [16, 16, 10, 9, 15, 19, 16.25, 12.5, 19],
    "mathematic": [14, 10, 15, 12, 13, 15.75, 16, 19, 14],
}
```

کلاس DataFrame وظیفه تبدیل داده ها به قالب جدول ( سطر و ستون ) دارد.

```python
import pandas as pd

dataSet = {
    "Name": [
        "Arash",
        "Shahram",
        "Omid",
        "Morteza",
        "Najme",
        "Mahsa",
        "Elham",
        "Maryam",
        "Sanam",
    ],
    "Physic ": [15, 15.25, 18, 17, 8, 14, 18, 17, 13],
    "chemistry": [16, 16, 10, 9, 15, 19, 16.25, 12.5, 19],
    "mathematic": [14, 10, 15, 12, 13, 15.75, 16, 19, 14],
}

df = pd.DataFrame(dataSet)
print(df)
```

![example-output](img/example-output.PNG)

متد sort_values، جدول براساس مولفه مشخص شده مرتب می کند. در این مثال می خواهیم جدول براساس ستون نام مرتب کنیم.

```python
import pandas as pd

dataSet = {
    "Name": [
        "Arash",
        "Shahram",
        "Omid",
        "Morteza",
        "Najme",
        "Mahsa",
        "Elham",
        "Maryam",
        "Sanam",
    ],
    "Physic ": [15, 15.25, 18, 17, 8, 14, 18, 17, 13],
    "chemistry": [16, 16, 10, 9, 15, 19, 16.25, 12.5, 19],
    "mathematic": [14, 10, 15, 12, 13, 15.75, 16, 19, 14],
}

df = pd.DataFrame(dataSet)
df = df.sort_values(
    by=["Name"]
)  # you can use "inplace=True" Instead of reassign to variable in argument.
print(df)

```

> 💡 دقت کنید، این متد به صورت پیش فرض، تغییرات به صورت موقت نگهداری می کند، به عبارت دیگر، اصل داده ای که در ورودی این متد تعریف شده، تغییر نمی کند، در نتیجه برای دسترسی به داده باید خروجی درون متغییر نگهداری کنیم.
>
> ```python
> df = df.sort_values(
>    by=["Name"]
> )
> ```
>
> برای نگهداری تغییرات به صورت دائمی، می توانیم مقدار "inplace=True" درون آرگومان تعریف کنیم. در نتیجه اصل داده، با تغییرات جدید ( جدول مرتب شده ) باز نویسی می شود.
>
> ```diff
> - df = df.sort_values(
> -     by=["Name"]
> - )
> + df.sort_values(by=["Name"], inplace=True)
> ```
>

![example-output-sortbyname](img/example-output-sortbyname.PNG)

📁 [مشاهده پروژه](project/2.students.py)



------

👋 Hi, I’m Arash Yeganeh.

How can you best ❤️ **Support me** ❤️  :

- Give me  [GitHub Stars ⭐](https://github.com/arashyeganeh) 
- Share my content to someone else 👀
- Follow me on [linkedin](https://www.linkedin.com/in/arash-yeganeh)
- Subscribe my [YouTube](https://www.youtube.com/channel/UCUuojnAmPiklBpAeBmHE4Aw) channel
