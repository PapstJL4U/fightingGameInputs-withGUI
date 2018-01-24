from os import sep

path = 'assets' + sep

_available = "\
\tlpmp, lphp, mphp, lkmk, lkhk, mkhk,\n\
\t2k, 2p, 3k, 3p,\n\
\tchargeback, chargedown,\n\
\tcomma[,], d, dash, down[2], downleft[1], downright[3],\n\
\tgreaterthan[>],\n\
\thcb, hcf, hk, hp, hs,\n\
\tk,\n\
\tleft[4], lk, lp,\n\
\tmk, mp,\n\
\tneutral[5],\n\
\tp, plus[+],\n\
\tqcb, qcf,\n\
\tright[6], rsrk,\n\
\ts, spd, srk,\n\
\ttilde[~],\n\
\tup[8], upleft[7], upright[9],\n\
\txx"

_input = {
    'lpmp': path + 'lpmp.png',
    'lphp': path + 'lphp.png',
    'mphp': path + 'mphp.png',
    'lkmk': path + 'lkmk.png',
    'lkhk': path + 'lkhk.png',
    'mkhk': path + 'mkhk.png',
    '2k': path + '2k.png',
    '2p': path + '2p.png',
    '3k': path + '3k.png',
    '3p': path + '3p.png',
    'chargeback': path + 'chargeback.png',
    'chargedown': path + 'chargedown.png',
    'comma': path + 'comma.png',
    'd': path + 'd.png',
    'dash': path + 'dash.png',
    'down': path + 'down.png',
    'downleft': path + 'downleft.png',
    'downright': path + 'downright.png',
    'greaterthan': path + 'greaterthan.png',
    'hcb': path + 'hcb.png',
    'hcf': path + 'hcf.png',
    'hk': path + 'hk.png',
    'hp': path + 'hp.png',
    'hs': path + 'hs.png',
    'k': path + 'k.png',
    'left': path + 'left.png',
    'lk': path + 'lk.png',
    'lp': path + 'lp.png',
    'mk': path + 'mk.png',
    'mp': path + 'mp.png',
    'neutral': path + 'neutral.png',
    'p': path + 'p.png',
    'plus': path + 'plus.png',
    'qcb': path + 'qcb.png',
    'qcf': path + 'qcf.png',
    'right': path + 'right.png',
    'rsrk': path + 'rsrk.png',
    'rdp': path + 'rsrk.png',
    's': path + 's.png',
    'spd': path + 'spd.png',
    'srk': path + 'srk.png',
    'dp': path + 'srk.png',
    'tilde': path + 'tilde.png',
    'up': path + 'up.png',
    'upleft': path + 'upleft.png',
    'upright': path + 'upright.png',
    'xx': path + 'xx.png',
}

_width = {
    'lpmp': 120,
    'lphp': 120,
    'mphp': 120,
    'lkmk': 120,
    'lkhk': 120,
    'mkhk': 120,
    '2k': 120,
    '2p': 120,
    '3k': 120,
    '3p': 120,
    'chargeback': 83,
    'chargedown': 50,
    'comma': 30,
    'd': 84,
    'dash': 76,
    'down': 52,
    'downleft': 60,
    'downright': 60,
    'greaterthan': 41,
    'hcb': 93,
    'hcf': 92,
    'hk': 86,
    'hp': 84,
    'hs': 82,
    'k': 85,
    'left': 72,
    'lk': 85,
    'lp': 84,
    'mk': 84,
    'mp': 84,
    'neutral': 56,
    'p': 86,
    'plus': 44,
    'qcb': 74,
    'qcf': 75,
    'right': 72,
    'rsrk': 65,
    'rdp': 65,
    's': 84,
    'spd': 85,
    'srk': 64,
    'dp': 64,
    'tilde': 44,
    'up': 50,
    'upleft': 60,
    'upright': 68,
    'xx': 71,
}
