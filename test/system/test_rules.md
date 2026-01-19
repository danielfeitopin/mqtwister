|                        Test Rule                        |          Input           |          Output          |
| :-----------------------------------------------------: | :----------------------: | :----------------------: |
|         `topic="test/set" payload.set("Test!")`         |    `"Hello, World!"`     |        `"Test!"`         |
|      `topic="test/lowercase" payload.lowercase()`       |    `"Hello, World!"`     |    `"hello, world!"`     |
|      `topic="test/uppercase" payload.uppercase()`       |    `"Hello, World!"`     |    `"HELLO, WORLD!"`     |
| `topic="test/replace" payload.replace("World", "Test")` |    `"Hello, World!"`     |     `"Hello, Test!"`     |
|   `topic="test/swap" payload.swap("Hello", "World")`    |    `"Hello, World!"`     |    `"World, Hello!"`     |
|     `topic="test/prepend" payload.prepend("Test ")`     |    `"Hello, World!"`     |  `"Test Hello, World!"`  |
|      `topic="test/append" payload.append(" Test")`      |    `"Hello, World!"`     |  `"Hello, World! Test"`  |
|           `topic="test/trim" payload.trim()`            |   `" Hello, World! "`    |    `"Hello, World!"`     |
|       `topic="test/truncate" payload.truncate(5)`       |    `"Hello, World!"`     |        `"Hello"`         |
|     `topic="test/to_int_str" payload.to_int_str()`      |         `"3.14"`         |          `"3"`           |
|   `topic="test/to_float_str" payload.to_float_str()`    |          `"3"`           |         `"3.0"`          |
|      `topic="test/to_base64" payload.to_base64()`       |    `"Hello, World!"`     | `"SGVsbG8sIFdvcmxkIQ=="` |
|    `topic="test/from_base64" payload.from_base64()`     | `"SGVsbG8sIFdvcmxkIQ=="` |    `"Hello, World!"`     |