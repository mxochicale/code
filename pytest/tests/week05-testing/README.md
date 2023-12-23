# week05-testing

## issues
```

pytest test_times.py 
=============================================================== test session starts ================================================================
platform linux -- Python 3.11.7, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/mxochicale/repositories/mxochicale/code/pytest/tests/week05-testing
plugins: mock-3.12.0
collected 7 items                                                                                                                                  

test_times.py ......F                                                                                                                        [100%]

===================================================================== FAILURES =====================================================================
_________________________________________________________________ test_iss_passes __________________________________________________________________

    def test_iss_passes():
        with mock.patch("requests.get", new=mock.MagicMock(return_value=ISS_response())) as mymock:
>           iss_over_London = iss_passes(51.5074, -0.1278)

test_times.py:61: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
times.py:35: in iss_passes
    return [(datetime.datetime.fromtimestamp(x['risetime']).strftime("%Y-%m-%d %H:%M:%S"),
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <dict_keyiterator object at 0x7f32b1822390>

>   return [(datetime.datetime.fromtimestamp(x['risetime']).strftime("%Y-%m-%d %H:%M:%S"),
             (datetime.datetime.fromtimestamp(x['risetime'] + x['duration'])).strftime("%Y-%m-%d %H:%M:%S"))
            for x in response]
E   TypeError: string indices must be integers, not 'str'

times.py:35: TypeError
--------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------
200
{'message': 'success', 'request': {'altitude': 10.0, 'datetime': 1703321064.740006, 'latitude': 51.5074, 'longitude': -0.1278, 'passes': 5}, 'response': [{'duration': 446, 'risetime': 1703409497.740006}, {'duration': 628, 'risetime': 1703415159.740006}, {'duration': 656, 'risetime': 1703420935.740006}, {'duration': 655, 'risetime': 1703426740.740006}, {'duration': 632, 'risetime': 1703432544.740006}]}
============================================================= short test summary info ==============================================================
FAILED test_times.py::test_iss_passes - TypeError: string indices must be integers, not 'str'
=========================================================== 1 failed, 6 passed in 0.14s =================================

```

## References
* https://github.com/UCL-COMP0233-22-23/times-tests
* https://github.com/UCL-MPHY0021-21-22/RSE-Classwork/issues/16
* https://gist.github.com/alessandrofelder/8fb8e34f29970cd8e05c4c18d30f98f5
`
