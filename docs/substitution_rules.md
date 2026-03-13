<!-- SPDX-FileCopyrightText: 2026 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>

SPDX-License-Identifier: CC-BY-SA-4.0 -->

# MQTwister substitution rule actions

<div>

| **Operation** | **Description**                                                                                                                                                                                  |
| :-----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|      set      | Replaces the original value in its entirety with the value of the parameter (bytes).                                                                                                             |
|   lowercase   | Converts the content to lowercase.                                                                                                                                                               |
|   uppercase   | Converts the content to uppercase.                                                                                                                                                               |
|    replace    | Replaces occurrences of the first argument (bytes) with the second argument (bytes). Accepts an optional third argument (int) as a counter of the maximum number of substitutions in the string. |
|     swap      | Swaps all appearances of the value of the first parameter (str) with the value of the second parameter (str).                                                                                    |
|    prepend    | Adds the value of the parameter (str) at the beginning of the original value.                                                                                                                    |
|    append     | Adds the value of the parameter (str) at the end of the original value.                                                                                                                          |
|     trim      | Removes blank spaces at the beginning and at the end.                                                                                                                                            |
|   truncate    | Truncates the value to the length specified by the parameter (int).                                                                                                                              |
|  to_int_str   | Attempts to convert a numeric character string (str) into another that represents an integer value.                                                                                              |
| to_float_str  | Attempts to convert a numeric character string (str) into another that represents a floating-point value.                                                                                        |
|   to_base64   | Encodes the value in Base64 format.                                                                                                                                                              |
|  from_base64  | Attempts to decode a Base64 value.                                                                                                                                                               |

</div>