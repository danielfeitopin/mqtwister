import mqtwister.lang.en as lang_en
import mqtwister.lang.es as lang_es
import mqtwister.lang.gl as lang_gl

def test_all_keys_present_in_lang_files():
    MESSAGES_EN = lang_en.MESSAGES
    MESSAGES_ES = lang_es.MESSAGES
    MESSAGES_GL = lang_gl.MESSAGES
    keys_en = set(MESSAGES_EN.keys())
    keys_es = set(MESSAGES_ES.keys())
    keys_gl = set(MESSAGES_GL.keys())
    assert keys_en == keys_es, "Some keys are missing in es.py compared to en.py"
    assert keys_en == keys_gl, "Some keys are missing in gl.py compared to en.py"