sklearn-pdtransform
-------------------

A little module with a few transformers to work with Pandas dataframes in the
Sklearn pipeline. Example usage:

.. code:: python
    pipeline = Pipeline([
        ('ordinal_to_nums', DFTransform(_ordinal_to_nums, copy=True)),
        ('union', DFFeatureUnion([
            ('categorical', Pipeline([
                ('select', DFTransform(lambda X: X.select_dtypes(include=['object']))),
                ('fill_na', DFTransform(lambda X: X.fillna('NA'))),
                ('one_hot', DFTransform(_one_hot_encode)),
            ])),
            ('numerical', Pipeline([
                ('select', DFTransform(lambda X: X.select_dtypes(exclude=['object']))),
                ('fill_median', DFTransform(lambda X: X.fillna(X.median()))),
                ('add_features', DFTransform(_add_features, copy=True)),
                ('remove_skew', DFTransform(_remove_skew, copy=True)),
                ('find_outliers', DFTransform(_find_outliers, copy=True)),
                ('normalize', DFTransform(lambda X: X.div(X.max())))
            ])),
        ])),
    ])


For more information read `this blog post <http://signal-to-noise.xyz/why-you-should-use-scikit-learns-pipeline-object.html>`_.
