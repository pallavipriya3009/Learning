__author__ = 'pallavipriya'

class Matrix( object ):
    def __init__(self, data, nrows, ncols ):
        self.nrows = nrows
        self.ncols = ncols
        self._fillData( data )

    def _fillData( self, data ):
        self.data = []
        for row in range( self.nrows ):
            rowData = []
            for col in range( self.ncols ):
                rowData.append( data[ row*self.ncols + col ] )
            self.data.append( rowData )

if __name__=='__main__':
    data = [1,2,3,4,5,6,7,8,9,10,11,12]
    print Matrix( data, 2, 6 ).data
    print Matrix( data, 3, 4 ).data
    print Matrix( data, 6, 2 ).data
    print Matrix( data, 4, 3 ).data
