
def is_entity(entry):
    """判断词单元是否实体
    Args:
        entry: WordUnit，词单元
    Returns:
        *: bool，实体(True)，非实体(False)
    """
    # 候选实体词性列表
    # 中科院词性标注标记集
    # nh: 人名
    # ni: 机构名
    # ns: 地名
    # nz: 其他专名
    # j: 简称
    entity_postags = {'nh', 'ni', 'ns', 'nz', 'j'}

    # HanLP
    # entity_postags = {'nr', 'nt', 'ns', 'nz', 'j'}
    return entry.postag in entity_postags \
           or entry.lemma in {"机动船", "帆船", "船舶", "船筏", "水上飞机", "航空器",
				"在航", "能见度"}

def like_noun(entry):
        """近似名词，根据词性标注判断此名词是否职位相关
        Args:
            entry: WordUnit，词单元
        Return:
            *: bool，判断结果，职位相关(True)，职位不相关(False)
        """
        #  'n'<--->general noun          'i'<--->idiom                 'j'<--->abbreviation
        # 'ni'<--->organization name    'nh'<--->person name          'nl'<--->location noun
        # 'ns'<--->geographical name    'nz'<--->other proper noun    'ws'<--->foreign words
        noun = {'n', 'i', 'j', 'ni', 'nh', 'nl', 'ns', 'nz', 'ws'}

        return entry.postag in noun