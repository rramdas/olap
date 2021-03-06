"""
select {([Measures].[Customer Count]), ([Measures].[Sales Count])} 
               * {([Time].[1997].[Q2].[4]), ([Time].[1997].[Q2].[5]) } on columns, 
        [Gender].[Gender].ALLMEMBERS on rows 
        from [Sales]

"""

result={'Axes': {'Axis': [{'Tuples': {'Tuple': [{'Member': [{'Caption': u'Customer Count',
                                                      'DisplayInfo': u'0',
                                                      'LName': u'[Measures].[MeasuresLevel]',
                                                      'LNum': u'0',
                                                      'UName': u'[Measures].[Customer Count]',
                                                      '_Hierarchy': u'Measures'},
                                                     {'Caption': u'4',
                                                      'DisplayInfo': u'0',
                                                      'LName': u'[Time].[Month]',
                                                      'LNum': u'2',
                                                      'UName': u'[Time].[1997].[Q2].[4]',
                                                      '_Hierarchy': u'Time'}]},
                                         {'Member': [{'Caption': u'Customer Count',
                                                      'DisplayInfo': u'0',
                                                      'LName': u'[Measures].[MeasuresLevel]',
                                                      'LNum': u'0',
                                                      'UName': u'[Measures].[Customer Count]',
                                                      '_Hierarchy': u'Measures'},
                                                     {'Caption': u'5',
                                                      'DisplayInfo': u'131072',
                                                      'LName': u'[Time].[Month]',
                                                      'LNum': u'2',
                                                      'UName': u'[Time].[1997].[Q2].[5]',
                                                      '_Hierarchy': u'Time'}]},
                                         {'Member': [{'Caption': u'Sales Count',
                                                      'DisplayInfo': u'0',
                                                      'LName': u'[Measures].[MeasuresLevel]',
                                                      'LNum': u'0',
                                                      'UName': u'[Measures].[Sales Count]',
                                                      '_Hierarchy': u'Measures'},
                                                     {'Caption': u'4',
                                                      'DisplayInfo': u'131072',
                                                      'LName': u'[Time].[Month]',
                                                      'LNum': u'2',
                                                      'UName': u'[Time].[1997].[Q2].[4]',
                                                      '_Hierarchy': u'Time'}]},
                                         {'Member': [{'Caption': u'Sales Count',
                                                      'DisplayInfo': u'0',
                                                      'LName': u'[Measures].[MeasuresLevel]',
                                                      'LNum': u'0',
                                                      'UName': u'[Measures].[Sales Count]',
                                                      '_Hierarchy': u'Measures'},
                                                     {'Caption': u'5',
                                                      'DisplayInfo': u'131072',
                                                      'LName': u'[Time].[Month]',
                                                      'LNum': u'2',
                                                      'UName': u'[Time].[1997].[Q2].[5]',
                                                      '_Hierarchy': u'Time'}]}]},
                    '_name': u'Axis0'},
                   {'Tuples': {'Tuple': [{'Member': {'Caption': u'F',
                                                     'DisplayInfo': u'0',
                                                     'LName': u'[Gender].[Gender]',
                                                     'LNum': u'1',
                                                     'UName': u'[Gender].[F]',
                                                     '_Hierarchy': u'Gender'}},
                                         {'Member': {'Caption': u'M',
                                                     'DisplayInfo': u'131072',
                                                     'LName': u'[Gender].[Gender]',
                                                     'LNum': u'1',
                                                     'UName': u'[Gender].[M]',
                                                     '_Hierarchy': u'Gender'}}]},
                    '_name': u'Axis1'}]},
 'CellData': {'Cell': [{'FmtValue': u'657',
                        'FormatString': u'#,###',
                        'Value': 657,
                        '_CellOrdinal': u'0'},
                       {'FmtValue': u'672',
                        'FormatString': u'#,###',
                        'Value': 672,
                        '_CellOrdinal': u'1'},
                       {'FmtValue': u'3.251',
                        'FormatString': u'#,###',
                        'Value': 3251,
                        '_CellOrdinal': u'2'},
                       {'FmtValue': u'3.438',
                        'FormatString': u'#,###',
                        'Value': 3438,
                        '_CellOrdinal': u'3'},
                       {'FmtValue': u'660',
                        'FormatString': u'#,###',
                        'Value': 660,
                        '_CellOrdinal': u'4'},
                       {'FmtValue': u'699',
                        'FormatString': u'#,###',
                        'Value': 699,
                        '_CellOrdinal': u'5'},
                       {'FmtValue': u'3.339',
                        'FormatString': u'#,###',
                        'Value': 3339,
                        '_CellOrdinal': u'6'},
                       {'FmtValue': u'3.428',
                        'FormatString': u'#,###',
                        'Value': 3428,
                        '_CellOrdinal': u'7'}]},
 'OlapInfo': {'AxesInfo': {'AxisInfo': [{'HierarchyInfo': [{'Caption': {'_name': u'[Measures].[MEMBER_CAPTION]'},
                                                            'DisplayInfo': {'_name': u'[Measures].[DISPLAY_INFO]'},
                                                            'LName': {'_name': u'[Measures].[LEVEL_UNIQUE_NAME]'},
                                                            'LNum': {'_name': u'[Measures].[LEVEL_NUMBER]'},
                                                            'UName': {'_name': u'[Measures].[MEMBER_UNIQUE_NAME]'},
                                                            '_name': u'Measures'},
                                                           {'Caption': {'_name': u'[Time].[MEMBER_CAPTION]'},
                                                            'DisplayInfo': {'_name': u'[Time].[DISPLAY_INFO]'},
                                                            'LName': {'_name': u'[Time].[LEVEL_UNIQUE_NAME]'},
                                                            'LNum': {'_name': u'[Time].[LEVEL_NUMBER]'},
                                                            'UName': {'_name': u'[Time].[MEMBER_UNIQUE_NAME]'},
                                                            '_name': u'Time'}],
                                         '_name': u'Axis0'},
                                        {'HierarchyInfo': {'Caption': {'_name': u'[Gender].[MEMBER_CAPTION]'},
                                                           'DisplayInfo': {'_name': u'[Gender].[DISPLAY_INFO]'},
                                                           'LName': {'_name': u'[Gender].[LEVEL_UNIQUE_NAME]'},
                                                           'LNum': {'_name': u'[Gender].[LEVEL_NUMBER]'},
                                                           'UName': {'_name': u'[Gender].[MEMBER_UNIQUE_NAME]'},
                                                           '_name': u'Gender'},
                                         '_name': u'Axis1'}]},
              'CellInfo': {'FmtValue': {'_name': u'FORMATTED_VALUE'},
                           'FormatString': {'_name': u'FORMAT_STRING'},
                           'Value': {'_name': u'VALUE'}},
              'CubeInfo': {'Cube': {'CubeName': u'Sales'}}},
 'schema': {'_elementFormDefault': u'qualified',
            '_targetNamespace': u'urn:schemas-microsoft-com:xml-analysis:mddataset',
            'complexType': [{'_name': u'MemberType',
                             'attribute': {'_name': u'Hierarchy',
                                           '_type': u'xsd:string'},
                             'sequence': {'element': [{'_name': u'UName',
                                                       '_type': u'xsd:string'},
                                                      {'_name': u'Caption',
                                                       '_type': u'xsd:string'},
                                                      {'_name': u'LName',
                                                       '_type': u'xsd:string'},
                                                      {'_name': u'LNum',
                                                       '_type': u'xsd:unsignedInt'},
                                                      {'_name': u'DisplayInfo',
                                                       '_type': u'xsd:unsignedInt'}],
                                          'sequence': {'_maxOccurs': u'unbounded',
                                                       '_minOccurs': u'0',
                                                       'any': {'_maxOccurs': u'unbounded',
                                                               '_processContents': u'lax'}}}},
                            {'_name': u'PropType',
                             'attribute': {'_name': u'name',
                                           '_type': u'xsd:string'}},
                            {'_name': u'TupleType',
                             'sequence': {'_maxOccurs': u'unbounded',
                                          'element': {'_name': u'Member',
                                                      '_type': u'MemberType'}}},
                            {'_name': u'MembersType',
                             'attribute': {'_name': u'Hierarchy',
                                           '_type': u'xsd:string'},
                             'sequence': {'_maxOccurs': u'unbounded',
                                          'element': {'_name': u'Member',
                                                      '_type': u'MemberType'}}},
                            {'_name': u'TuplesType',
                             'sequence': {'_maxOccurs': u'unbounded',
                                          'element': {'_name': u'Tuple',
                                                      '_type': u'TupleType'}}},
                            {'_name': u'CrossProductType',
                             'attribute': {'_name': u'Size',
                                           '_type': u'xsd:unsignedInt'},
                             'sequence': {'choice': {'_maxOccurs': u'unbounded',
                                                     '_minOccurs': u'0',
                                                     'element': [{'_name': u'Members',
                                                                  '_type': u'MembersType'},
                                                                 {'_name': u'Tuples',
                                                                  '_type': u'TuplesType'}]}}},
                            {'_name': u'OlapInfo',
                             'sequence': {'element': [{'_name': u'CubeInfo',
                                                       'complexType': {'sequence': {'element': {'_maxOccurs': u'unbounded',
                                                                                                '_name': u'Cube',
                                                                                                'complexType': {'sequence': {'element': {'_name': u'CubeName',
                                                                                                                                         '_type': u'xsd:string'}}}}}}},
                                                      {'_name': u'AxesInfo',
                                                       'complexType': {'sequence': {'element': {'_maxOccurs': u'unbounded',
                                                                                                '_name': u'AxisInfo',
                                                                                                'complexType': {'attribute': {'_name': u'name',
                                                                                                                              '_type': u'xsd:string'},
                                                                                                                'sequence': {'element': {'_maxOccurs': u'unbounded',
                                                                                                                                         '_minOccurs': u'0',
                                                                                                                                         '_name': u'HierarchyInfo',
                                                                                                                                         'complexType': {'attribute': {'_name': u'name',
                                                                                                                                                                       '_type': u'xsd:string',
                                                                                                                                                                       '_use': u'required'},
                                                                                                                                                         'sequence': {'sequence': [{'_maxOccurs': u'unbounded',
                                                                                                                                                                                    'element': [{'_name': u'UName',
                                                                                                                                                                                                 '_type': u'PropType'},
                                                                                                                                                                                                {'_name': u'Caption',
                                                                                                                                                                                                 '_type': u'PropType'},
                                                                                                                                                                                                {'_name': u'LName',
                                                                                                                                                                                                 '_type': u'PropType'},
                                                                                                                                                                                                {'_name': u'LNum',
                                                                                                                                                                                                 '_type': u'PropType'},
                                                                                                                                                                                                {'_maxOccurs': u'unbounded',
                                                                                                                                                                                                 '_minOccurs': u'0',
                                                                                                                                                                                                 '_name': u'DisplayInfo',
                                                                                                                                                                                                 '_type': u'PropType'}]},
                                                                                                                                                                                   {'any': {'_maxOccurs': u'unbounded',
                                                                                                                                                                                            '_minOccurs': u'0',
                                                                                                                                                                                            '_processContents': u'lax'}}]}}}}}}}}},
                                                      {'_name': u'CellInfo',
                                                       'complexType': {'sequence': {'sequence': [{'_maxOccurs': u'unbounded',
                                                                                                  '_minOccurs': u'0',
                                                                                                  'choice': {'element': [{'_name': u'Value',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'FmtValue',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'BackColor',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'ForeColor',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'FontName',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'FontSize',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'FontFlags',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'FormatString',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'NonEmptyBehavior',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'SolveOrder',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'Updateable',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'Visible',
                                                                                                                          '_type': u'PropType'},
                                                                                                                         {'_name': u'Expression',
                                                                                                                          '_type': u'PropType'}]}},
                                                                                                 {'_maxOccurs': u'unbounded',
                                                                                                  '_minOccurs': u'0',
                                                                                                  'any': {'_maxOccurs': u'unbounded',
                                                                                                          '_processContents': u'lax'}}]}}}]}},
                            {'_name': u'Axes',
                             'sequence': {'_maxOccurs': u'unbounded',
                                          'element': {'_name': u'Axis',
                                                      'complexType': {'attribute': {'_name': u'name',
                                                                                    '_type': u'xsd:string'},
                                                                      'choice': {'_maxOccurs': u'unbounded',
                                                                                 '_minOccurs': u'0',
                                                                                 'element': [{'_name': u'CrossProduct',
                                                                                              '_type': u'CrossProductType'},
                                                                                             {'_name': u'Tuples',
                                                                                              '_type': u'TuplesType'},
                                                                                             {'_name': u'Members',
                                                                                              '_type': u'MembersType'}]}}}}},
                            {'_name': u'CellData',
                             'sequence': {'element': {'_maxOccurs': u'unbounded',
                                                      '_minOccurs': u'0',
                                                      '_name': u'Cell',
                                                      'complexType': {'attribute': {'_name': u'CellOrdinal',
                                                                                    '_type': u'xsd:unsignedInt',
                                                                                    '_use': u'required'},
                                                                      'sequence': {'_maxOccurs': u'unbounded',
                                                                                   'choice': {'element': [{'_name': u'Value'},
                                                                                                          {'_name': u'FmtValue',
                                                                                                           '_type': u'xsd:string'},
                                                                                                          {'_name': u'BackColor',
                                                                                                           '_type': u'xsd:unsignedInt'},
                                                                                                          {'_name': u'ForeColor',
                                                                                                           '_type': u'xsd:unsignedInt'},
                                                                                                          {'_name': u'FontName',
                                                                                                           '_type': u'xsd:string'},
                                                                                                          {'_name': u'FontSize',
                                                                                                           '_type': u'xsd:unsignedShort'},
                                                                                                          {'_name': u'FontFlags',
                                                                                                           '_type': u'xsd:unsignedInt'},
                                                                                                          {'_name': u'FormatString',
                                                                                                           '_type': u'xsd:string'},
                                                                                                          {'_name': u'NonEmptyBehavior',
                                                                                                           '_type': u'xsd:unsignedShort'},
                                                                                                          {'_name': u'SolveOrder',
                                                                                                           '_type': u'xsd:unsignedInt'},
                                                                                                          {'_name': u'Updateable',
                                                                                                           '_type': u'xsd:unsignedInt'},
                                                                                                          {'_name': u'Visible',
                                                                                                           '_type': u'xsd:unsignedInt'},
                                                                                                          {'_name': u'Expression',
                                                                                                           '_type': u'xsd:string'}]}}}}}}],
            'element': {'_name': u'root',
                        'complexType': {'sequence': {'_maxOccurs': u'unbounded',
                                                     'element': [{'_name': u'OlapInfo',
                                                                  '_type': u'OlapInfo'},
                                                                 {'_name': u'Axes',
                                                                  '_type': u'Axes'},
                                                                 {'_name': u'CellData',
                                                                  '_type': u'CellData'}]}}}}}
