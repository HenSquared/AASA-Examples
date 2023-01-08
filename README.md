<!-- About the Project -->
## About the Project

AASA-Examples is examples of [Apple App Site Association](https://developer.apple.com/documentation/xcode/supporting-associated-domains) files from several companies and organizations.

#### You can use this project to 
- Better understand how AASA files work
- Research other organizations features and deeplinks

Some companies have quite small AASA files:

Telegram.json
```
{
    "applinks": {
        "apps": [],
        "details": [
            {
                "appID": "X834Q8SBVP.org.telegram.TelegramEnterprise",
                "paths": [
                    "*"
                ]
            },
            {
                "appID": "C67CF9S4VU.ph.telegra.Telegraph",
                "paths": [
                    "*"
                ]
            },
            {
                "appID": "X834Q8SBVP.org.telegram.Telegram-iOS",
                "paths": [
                    "*"
                ]
            }
        ]
    }
}
```

While others are much more large:
```bash
$ wc -l aasa_examples/amazon.json
3170 aasa_examples/amazon.json
```
<!-- Prerequisites -->
###  Prerequisites

This project uses python3 standard libraries. 

<!-- Run -->
### Run

Clone the project

```bash
  git clone https://github.com/hensquared/aasa-examples.git
```

Go to the project directory

```bash
  cd aasa-examples
```

Run the project

```bash
  python3 main.py
```

<!-- Contributing -->
### Contributing

I welcome additional examples of AASA files. 

1. Add a URL and name to urls.csv
2. Rerun the project. 
3. Check for errors
3. If no errors, open a PR with your additions. 

Thanks!


