class BigNumberManager:
    def format_big_num(self, number) -> str:
        large_num_dict = {
            6: 'M',
            9: 'B',
            12: 'T',
            15: 'Qa',
            18: 'Qi',
            21: 'Sx',
            24: 'Sp',
            27: 'Oc',
            30: 'Nm',
            33: 'Dc'
        }
        str_num = str(number)
        length = len(str_num)
        if length <= 3:
            sig_digs = str_num
        else:
            if length % 3 == 0:
                sig_digs = str_num[:3]
            else:
                sig_digs = str_num[:length % 3]
        return f"{sig_digs} {large_num_dict[length - len(str(sig_digs))]}"
