import unittest
import mock
import os
import sys
path = os.path.join(os.path.dirname(__file__), '../src')
sys.path.append(path)
import src.randomizer as rm
import original_exc


# 'python -m unittest *.py'で実行することができる
class TestFormatter(unittest.TestCase):
    # 複数人チャンネルにいた場合のテスト
    @mock.patch('random.sample')
    def test_get_random_order(self, random_call):
        A = mock.MagicMock(name="A")
        B = mock.MagicMock(name="B")
        C = mock.MagicMock(name="C")
        D = mock.MagicMock(name="D")
        E = mock.MagicMock(name="E")

        channel_members = [A, B, C, D, E]
        random_call.return_value = [2, 3, 4, 1, 0]
        member_dct = rm.get_random_order(channel_members)
        self.assertEqual([(0, E.name), (1, D.name), (2, A.name), (3, B.name),
                          (4, C.name)], member_dct)

    # 一人のみチャンネルにいた場合のテスト
    def test_get_random_order_single(self):
        A = mock.MagicMock(name="A")

        channel_members = [A]
        member_dct = rm.get_random_order(channel_members)
        self.assertEqual([(0, A.name)], member_dct)

    # 誰もチャンネルにいない場合のテスト
    def test_get_random_order_exception(self):
        channel_members = []
        with self.assertRaises(original_exc.NoMemberInVoiceChannelException):
            rm.get_random_order(channel_members)
